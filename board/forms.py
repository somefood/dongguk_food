from django import forms
from .models import UserBoard, Comment


class BoardForm(forms.ModelForm):
    class Meta:
        model = UserBoard
        fields = ('title', 'content')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '제목을 입력해주세요.'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'id': 'post_content', 'placeholder': '내용을 입력해주세요.'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text', )
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'id': 'inputComment', 'rows': '3', 'style': 'resize:none;'}),
        }