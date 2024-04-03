
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UserRegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# user_profile/views.py

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ProfileForm  # Import the ProfileForm

@login_required
def profile_view(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('user_profile:profile')
    else:
        form = ProfileForm(instance=request.user.profile)
    
    return render(request, 'user_profile/profile.html', {'form': form})

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

def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_profile:login')  # Redirect to login page after successful registration
    else:
        form = UserRegistrationForm()
    
    return render(request, 'user_profile/register.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS, 'You have successfully logged out.')
    return redirect('/user_profile/login/')
