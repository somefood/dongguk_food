from django.urls import path

from . import views

app_name = 'cs_service'

urlpatterns = [
    path('', views.index, name='index'),
    path('terms/', views.terms, name='terms'),
    path('voice/', views.voice, name='voice'),
]