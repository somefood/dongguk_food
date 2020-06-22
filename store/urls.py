from django.urls import path
from . import views

app_name = 'store'
urlpatterns = [
    path('', views.StoreIndexView.as_view(), name='index'),
    path('detail/<str:slug>', views.StoreDetailView.as_view(), name='detail'),
    path('detail/like/<int:pk>', views.store_like, name='like'),
    path('create/', views.StoreCreateView.as_view(), name='create'),
    path('edit/<str:slug>', views.StoreEditView.as_view(), name='edit'),
    path('delete/<str:slug>', views.StoreDeleteView.as_view(), name='delete'),
]