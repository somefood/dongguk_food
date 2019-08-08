from django.urls import path

from . import views

app_name='accounts'
urlpatterns = [
	path('signin/', views.signin, name='signin'),
	path('signout/', views.signout, name='signout'),
	path('signup/', views.signup, name='signup'),
    #path('signup/', views.SignUp.as_view(), name='signup'),
]
