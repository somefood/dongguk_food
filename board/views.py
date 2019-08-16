from django.shortcuts import render
from .models import UserBoard
from .forms import BoardForm

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
