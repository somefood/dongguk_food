from django.urls import path
from . import views

app_name = 'store'
urlpatterns = [
    path('', views.StoreIndexView.as_view(), name='index'),
    path('<str:category>/', views.CategoryView.as_view(), name='category'),
    path('like/', views.like, name='like'),
    path('detail/<str:slug>/', views.StoreDetailView.as_view(), name='detail'),
    path('detail/<str:slug>/comment/create/', views.comment_create, name='comment_create'),
    path('create/', views.StoreCreateView.as_view(), name='store_add'),
    path('edit/<int:pk>/', views.StoreEditView.as_view(), name='store_edit'),
    path('delete/<int:pk>/', views.StoreDeleteView.as_view(), name='store_delete'),
]