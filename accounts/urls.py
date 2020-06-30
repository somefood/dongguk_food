from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
	path('login/', views.signin, name='login'),
	path('logout/', views.signout, name='logout'),
	path('signup/', views.signup, name='signup'),
	path('mypage/', views.MyPageV.as_view(), name='mypage'),
	path('checkuser/', views.check_user, name='check_user'),
	path('checknickname/', views.check_nickname, name='check_nickname'),
]
