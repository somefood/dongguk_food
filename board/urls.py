from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('', views.index, name='index'),
    path('insert/', views.check_post, name='board_insert'),
]
