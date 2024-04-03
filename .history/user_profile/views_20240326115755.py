
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UserRegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse
from django.contrib.auth import logout
from django.contrib import messages

# You might want to pass context or user-specific data here
def profile_view(request):
    context = {'message': 'This is your profile page.'}
    return render(request, 'user_profile/profile.html', context)

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to login page after successful registration
            return redirect('user_profile:login')  # Using redirect with the name of the login url pattern
    else:
        form = UserRegistrationForm()
    return render(request, 'user_profile/register.html', {'form': form, 'show_navbar': False})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # Redirect to the th_monitoring page
            return redirect('th_monitoring:dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'user_profile/login.html', {'form': form, 'show_navbar': False})

# user_profile/views.py

def logout_view(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS, 'You have successfully logged out.')
    return redirect('/user_profile/login/')
