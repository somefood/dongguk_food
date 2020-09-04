from django import forms
from .models import Store, Menu, Comment
from django.forms import inlineformset_factory

MenuInlineFormSet = inlineformset_factory(Store, Menu,
                                          fields=['name', 'description', 'food_image'],
                                          extra=2)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text', )
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'id': 'inputComment', 'rows': '3', 'style': 'resize:none;'}),
        }