from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import UserBoard
from .forms import BoardForm
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

class BoardIndex(ListView):
    template_name = 'board/index.html'
    context_object_name = 'board_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context

    def get_queryset(self):
        return UserBoard.objects.all()

@login_required
def post_new(request):
    template_name = 'board/board_success.html'
    if request.method == "POST":
        print(request.POST)
        username = request.user
        form = BoardForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            user = User.objects.get(username=username)
            item.writer = user
            item.board_save()
            message = "항목을 추가하였습니다."
            return render(request, template_name, {"message": message})
    else:
        template_name = 'board/post.html'
        form = BoardForm
        print(request.GET)
        print(request.user.profile.nickname)
        return render(request, template_name, {"form": form})

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
    return render(request, 'board/post.html', {"form": form})

# def test(request, pk):
#     return HttpResponse('hi {}'.format(pk))

def post_delete(request, pk):
    post = get_object_or_404(UserBoard, pk=pk)
    post.delete()
    return redirect('board:index')

class BoardDetail(DetailView):
    model = UserBoard
    template_name = 'board/detail.html'