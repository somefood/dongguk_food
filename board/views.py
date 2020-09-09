from django.core.paginator import Paginator
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from .models import UserBoard, Comment
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


class CommentListView(ListView):
    model = Comment
    paginate_by = 5
    template_name = '_comment_list.html'
    context_object_name = 'comment_list'

    def get_queryset(self):
        store = get_object_or_404(UserBoard, slug=self.kwargs['slug'])
        return store.comment_set.all()

    def get_context_data(self, *args, **kwargs):
        store = get_object_or_404(UserBoard, slug=self.kwargs['slug'])
        context = super().get_context_data(*args, **kwargs)
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
        context['store'] = store
        return context


@login_required
def comment_create(request, slug):
    if not request.user.is_authenticated:
        return JsonResponse({'authenticated': False})
    post = get_object_or_404(UserBoard, slug=slug)
    form = CommentForm(request.POST)
    if form.is_valid():
        form.instance.writer = request.user
        form.instance.post = post
        form.save()
    paginator = Paginator(post.comment_set.all(), 5)
    last_page = paginator.num_pages
    return JsonResponse({'last_page': last_page, 'authenticated': True})


@login_required
def comment_update(request, slug, pk):
    store = get_object_or_404(UserBoard, slug=slug)
    comment = store.comment_set.get(pk=pk)
    if comment.writer == request.user:
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save()
            html = render_to_string('_comment_update.html', {'comment': comment} )
            return JsonResponse({'is_updated': True, 'html': html})


@login_required
def comment_delete(request, slug, pk):
    store = get_object_or_404(UserBoard, slug=slug)
    comment = store.comment_set.get(pk=pk)
    if comment.writer == request.user:
        comment.delete()
    return JsonResponse({'is_deleted': True})


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