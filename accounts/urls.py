from django.urls import path
from . import views

app_name='accounts'
urlpatterns = [
	path('login/', views.signin, name='login'),
	path('logout/', views.signout, name='logout'),
	path('signup/', views.signup, name='signup'),
    #path('signup/', views.SignUp.as_view(), name='signup'),
]
