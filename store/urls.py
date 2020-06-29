from django.urls import path
from . import views

app_name = 'store'
urlpatterns = [
    path('', views.StoreIndexView.as_view(), name='index'),
    path('index/<str:category>/', views.CategoryView.as_view(), name='category'),
    path('detail/<str:slug>/', views.StoreDetailView.as_view(), name='detail'),
    path('detail/like/<int:pk>/', views.store_like, name='like'),
    path('create/', views.StoreCreateView.as_view(), name='store_add'),
    path('edit/<int:pk>/', views.StoreEditView.as_view(), name='edit'),
    path('delete/<int:pk>/', views.StoreDeleteView.as_view(), name='delete'),
]