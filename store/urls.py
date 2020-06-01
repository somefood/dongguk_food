from django.urls import path

from . import views

app_name = 'store'
urlpatterns = [
    path('', views.StoreIndex.as_view(), name='index'),
    path('detail/<int:pk>', views.StoreDetail.as_view(), name='detail'),
]