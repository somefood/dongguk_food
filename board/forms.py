from django import forms
from .models import UserBoard

class BoardForm(forms.ModelForm):
    class Meta:
        model = UserBoard
        fields = ('title', 'writer', 'mail')
