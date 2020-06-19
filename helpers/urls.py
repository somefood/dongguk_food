from django.urls import path
from . import views

app_name='helpers'
urlpatterns = [
    path('search/', views.search_word, name='search')
    # path('search/<str:searchWord>/', views.SearchFormView.as_view(), name='search')
]