from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.urls import reverse_lazy
from .models import UserBoard
from .forms import BoardForm
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from mysite.views import OwnerOnlyMixin
from django.views.generic import CreateView, UpdateView, DeleteView
from django.conf import settings

class BoardIndex(ListView):
    template_name = 'board/index.html'
    context_object_name = 'board_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context

    def get_queryset(self):
        return UserBoard.objects.all()

class BoardCreateV(LoginRequiredMixin, CreateView):
    model = UserBoard
    fields = ('title', 'content')
    success_url = reverse_lazy('board:index')
    template_name = 'board/board_form.html'

    def form_valid(self, form):
        form.instance.writer = self.request.user
        return super().form_valid(form)


class BoardUpdateV(OwnerOnlyMixin, UpdateView):
    model = UserBoard
    fields = ('title', 'content')
    template_name = 'board/board_form.html'

class BoardDeleteV(OwnerOnlyMixin, DeleteView):
    model = UserBoard
    success_url = reverse_lazy('board:index')
    template_name = 'board/board_confirm_delete.html'

@login_required
def post_edit(request, pk):
    post = get_object_or_404(UserBoard, pk=pk)
    if request.method == "POST":
        form = BoardForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            post.save()
            return HttpResponseRedirect(reverse('board:detail', kwargs={'pk':pk}))
    else:
        form = BoardForm(instance=post)
    return render(request, 'board/board_form.html', {"form": form})

# def test(request, pk):
#     return HttpResponse('hi {}'.format(pk))

def post_delete(request, pk):
    post = get_object_or_404(UserBoard, pk=pk)
    post.delete()
    return redirect('board:index')

class BoardDetail(DetailView):
    model = UserBoard
    template_name = 'board/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['disqus_short'] = f"{settings.DISQUS_SHORTNAME}"
        context['disqus_id'] = f"post-{self.object.id}-{self.object.slug}"
        context['disqus_url'] = f"{settings.DISQUS_MY_DOMAIN}{self.object.get_absolute_url()}"
        context['disqus_title'] = f"{self.object.slug}"
        return context