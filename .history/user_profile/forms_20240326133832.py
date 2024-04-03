from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model
from .models import User

User = get_user_model()

# class UserRegistrationForm(UserCreationForm):
#     email = forms.EmailField()
#     first_name = forms.CharField(max_length=30)
#     last_name = forms.CharField(max_length=30)

#     class Meta:
#         model = User
#         fields = ['email', 'first_name', 'last_name', 'password1', 'password2']

class UserRegistrationForm(forms.ModelForm):


class ProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']

class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username', }) )
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password', }))
