from django.shortcuts import render, get_object_or_404
from .models import UserBoard
from .forms import BoardForm
from django.views import generic
from django.http import HttpResponse

def index(request):
    board_list = UserBoard.objects.all()
    return render(request, 'board/board_list.html', {"board_list": board_list})

def check_post(request):
    template_name = 'board/board_success.html'
    if request.method == "POST":
        form = BoardForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.board_save()
            message = "항목을 추가하였습니다."
            return render(request, template_name, {"message":message})
    else:
        template_name = 'board/insert.html'
        form = BoardForm
        return render(request, template_name, {"form":form})

# def test(request, pk):
#     return HttpResponse('hi {}'.format(pk))


class BoardDetail(generic.DetailView):
    model = UserBoard
    template_name = 'board/board_detail.html'
    context_object_name = 'board_list'
#     def get_object(self):
#         object = get_object_or_404(UserBoard, id=self.kwargs['pk'])
#         return object
    # def get_queryset(self):
    #     return UserBoard.objects.order_by('-created_date')[5:]