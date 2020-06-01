from django import forms
from .models import UserBoard

class BoardForm(forms.ModelForm):
    class Meta:
        model = UserBoard
        fields = ('title', 'content')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '제목을 입력해주세요.'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'id': 'post_content', 'placeholder': '내용을 입력해주세요.'}),
        }