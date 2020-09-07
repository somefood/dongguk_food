from django.urls import path
from . import views

app_name = 'board'
urlpatterns = [
    path('', views.BoardIndex.as_view(), name='index'),
    path('detail/<str:slug>/', views.BoardDetail.as_view(), name='detail'),
    path('detail/<str:slug>/comment/create/', views.comment_create, name='comment_create'),
    path('detail/<str:slug>/comment/', views.CommentListView.as_view(), name='comment'),
    path('detail/<str:slug>/comment/create/', views.comment_create, name='comment_create'),
    path('detail/<str:slug>/comment/delete/<int:pk>', views.comment_delete, name='comment_delete'),
    path('like/', views.like, name='like'),
    path('post/new/', views.BoardCreateV.as_view(), name='post_add'),
    path('post/edit/<int:pk>/', views.BoardUpdateV.as_view(), name='post_edit'),
    path('post/delete/<int:pk>/', views.BoardDeleteV.as_view(), name='post_delete'),
]
