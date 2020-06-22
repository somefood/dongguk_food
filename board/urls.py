from django.urls import path
from . import views

app_name = 'board'
urlpatterns = [
    path('', views.BoardIndex.as_view(), name='index'),
    path('post/<str:slug>', views.BoardDetail.as_view(), name='detail'),
    # path('post/new/', views.post_new, name='post_new'),
    path('post/new/', views.BoardCreateV.as_view(), name='post_new'),
    # path('post/edit/<int:pk>', views.post_edit, name='post_edit'),
    path('post/edit/<int:pk>/', views.BoardUpdateV.as_view(), name='post_edit'),
    # path('post/delete/<int:pk>', views.post_delete, name='post_delete'),
    path('post/delete/<int:pk>/', views.BoardDeleteV.as_view(), name='post_delete'),
]
