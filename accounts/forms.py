from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')
    telegram = forms.CharField(max_length=100, help_text='Required. Enter your Telegram username.')

    class Meta:
        model = User
        fields = ('username', 'email', 'telegram', 'password1', 'password2')