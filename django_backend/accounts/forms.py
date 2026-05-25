from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)
    age = forms.IntegerField(required=False, min_value=10, max_value=100)

    class Meta:
        model = User
        fields = ('username', 'email', 'age', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    pass
