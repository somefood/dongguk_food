from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.urls import reverse_lazy
from .models import UserBoard
from .forms import CommentForm
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from mysite.views import OwnerOnlyMixin
from django.views.generic import CreateView, UpdateView, DeleteView
from django.views.generic.edit import FormMixin
from django.conf import settings
from django.http import JsonResponse
import json


class BoardIndex(ListView):
    template_name = 'board/index.html'
    context_object_name = 'board_list'
    paginate_by = 10

    def get_queryset(self):
        return UserBoard.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = context['paginator']
        page_numbers_range = 5  # Display only 5 page numbers
        max_index = len(paginator.page_range)

        page = self.request.GET.get('page')
        current_page = int(page) if page else 1
        start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
        end_index = start_index + page_numbers_range
        if end_index >= max_index:
            end_index = max_index

        page_range = paginator.page_range[start_index:end_index]
        context['page_range'] = page_range
        return context


class BoardCreateV(LoginRequiredMixin, CreateView):
    model = UserBoard
    fields = ('title', 'content', 'tags')
    success_url = reverse_lazy('board:index')
    template_name = 'board/board_form.html'

    def form_valid(self, form):
        form.instance.writer = self.request.user
        return super().form_valid(form)


class BoardUpdateV(OwnerOnlyMixin, UpdateView):
    model = UserBoard
    fields = ('title', 'content', 'tags')
    template_name = 'board/board_form.html'


class BoardDeleteV(OwnerOnlyMixin, DeleteView):
    model = UserBoard
    success_url = reverse_lazy('board:index')
    template_name = 'board/board_confirm_delete.html'


class BoardDetail(FormMixin, DetailView):
    model = UserBoard
    form_class = CommentForm
    template_name = 'board/detail.html'

    def get_success_url(self):
        return reverse('board:detail', args=[self.object.slug])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        context['comments'] = self.object.comment_set.all()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if not request.user.is_authenticated:
            return self.render_to_response(self.get_context_data(form=form))

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.post = get_object_or_404(UserBoard, pk=self.object.pk)
        comment.writer = self.request.user
        comment.save()
        return render(self.request, '_comment.html', {'comment': comment})
        # return JsonResponse({"success": True, "content": str(comment.text), "writer": str(comment.writer), "date": str(comment.created)}, status=200)


@login_required
def like(request):
    pk = request.GET.get('pk', None)
    board = get_object_or_404(UserBoard, pk=pk)

    if request.user in board.like_users.all():
        board.like_users.remove(request.user)
        board.like_count -= 1
        board.save()
        message = False
    else:
        board.like_users.add(request.user)
        board.like_count += 1
        board.save()
        message = True
    context = {
        'like_count': board.like_users.count(),
        'message': message,
        'nickname': request.user.nickname
    }
    return HttpResponse(json.dumps(context), content_type="application/json")