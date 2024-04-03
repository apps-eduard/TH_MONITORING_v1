from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2']
# forms.py
from django import forms
from .models import User

class ProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']
