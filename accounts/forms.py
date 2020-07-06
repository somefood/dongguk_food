from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import User


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email', 'nickname', 'phone_number', )


class FindUserForm(forms.Form):
    nickname = forms.CharField(max_length=30, label='닉네임', widget=forms.TextInput(attrs=
                                                                                  {'placeholder': '닉네임을 입력해주세요.',
                                                                                   'class': 'form-control'}))
    phone_number = forms.CharField(max_length=30, label='전화번호', widget=forms.TextInput(attrs=
                                                                                       {'placeholder': '전화번호를 입력해주세요.',
                                                                                        'class': 'form-control'}))