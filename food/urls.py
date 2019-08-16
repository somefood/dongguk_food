from django.urls import path

from . import views

app_name = 'food'
urlpatterns = [
    path('', views.index, name='index'),
    path('recom/<int:store_id>', views.recom, name='recom'),
]