from django.forms import ModelForm
from .models import Store, Menu
from django.forms import inlineformset_factory

MenuInlineFormSet = inlineformset_factory(Store, Menu,
                                          fields=['name', 'description', 'food_image'],
                                          extra=2)