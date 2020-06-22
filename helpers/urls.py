from django.urls import path
from . import views

app_name='helpers'
urlpatterns = [
    path('search/', views.search_word, name='search'),
    path('tag/', views.TagCloudTV.as_view(), name='tag_cloud'),
    path('tag/<str:tag>/', views.TaggedObjectLV.as_view(), name='tagged_object_list'),
]