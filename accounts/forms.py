from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Profile
from django import forms


class SignupForm(ModelForm): #회원가입을 제공하는 class이다.
    password_check = forms.CharField(max_length=200, widget=forms.PasswordInput(attrs={
        'placeholder': '비밀번호를 한 번 더 입력해주세요.', 'class': 'form-control', 'id': 'loginPW-check'}))
    # 아쉽게도 User 모델에서는 password_check 필드를 제공해주지 않는다.
    # 따라서 따로 password_check 필드를 직접 정의해줄 필요가 있다.
    # 입력 양식은 type은 기본이 text이다. 따라서 다르게 지정해주고 싶을 경우 widget을 이용한다.
    # widget=forms.PasswordInput()은 입력 양식을 password로 지정해주겠다는 뜻이다.

    field_order = ['username', 'password', 'password_check', 'email']
    # field_order=['username','password','password_check','last_name','first_name','email']
    # field_order는 만들어지는 입력양식의 순서를 정해준다.
    # 여기서 사용한 이유는 password 바로 밑에 password_check 입력양식을 추가시키고 싶어서이다.
    # 만약 따로 field_order를 지정해주지않았다면, password_check는 맨 밑에 생성된다.
    class Meta:
        model = User
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': '아이디를 입력해주세요.','id': 'loginID', 'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'placeholder': '비밀번호를 입력해주세요.', 'id': 'loginPW', 'class': 'form-control'}),
            # 'password_check': forms.PasswordInput(attrs={'placeholder': '비밀번호를 입력해주세요.', 'class': 'signName'}),
        }
        fields = ['username', 'password', 'password_check', 'email']
#User model에 정의된 username, passwordm last_name, first_name, email을 입력양식으로

class SigninForm(ModelForm): #로그인을 제공하는 class이다.
    class Meta:
        model = User
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'id': 'loginID', 'placeholder': '아이디를 입력해주세요.'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'id': 'loginPW', 'placeholder': '패스워드를 입력해주세요.'})
        }
        fields = ['username', 'password']

class ProfileForm(ModelForm):
    # address = forms.CharField(widget=forms.RadioSelect())
    class Meta:
        model = Profile
        fields = ['nickname', 'phone_number',]
        widgets = {
            'nickname': forms.TextInput(attrs={'placeholder': '닉네임을 입력해주세요.', 'class': 'form-control', 'id': 'nickName'}),
            'phone_number': forms.TextInput(attrs={'placeholder': '전화번호를 입력해주세요.', 'class': 'form-control', 'id': 'phoneNumber'}),
        }