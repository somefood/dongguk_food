from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('', views.index, name='index'),
    path('insert/', views.check_post, name='board_insert'),
    path('<int:pk>/detail/', views.BoardDetail.as_view(), name='board_detail'),
]
