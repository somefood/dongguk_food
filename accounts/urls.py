from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
	path('login/', views.UserLoginView.as_view(), name='login'),
	path('logout/', views.signout, name='logout'),
	path('signup/', views.UserSignUpView.as_view(), name='signup'),
	path('signup/done/', views.UserSignUpDoneView.as_view(), name='signup_done'),
	path('mypage/', views.MyPageV.as_view(), name='mypage'),
	path('checkuser/', views.check_user, name='check_user'),
	path('checknickname/', views.check_nickname, name='check_nickname'),
	path('finduser/', views.FindUser.as_view(), name='find_user')
]