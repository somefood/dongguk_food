from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from accounts.models import User


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('nickname', 'phone_number', )