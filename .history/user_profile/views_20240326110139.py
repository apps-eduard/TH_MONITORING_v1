
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UserRegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse

# You might want to pass context or user-specific data here
def profile_view(request):
    context = {'message': 'This is your profile page.'}
    return render(request, 'user_profile/profile.html', context)

def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to login page after successful registration
            return redirect('login')  # Using redirect with the name of the login url pattern
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
            return redirect('th_monitoring:index'))  # Adjust 'th_monitoring:index' as necessary
    else:
        form = AuthenticationForm()
    return render(request, 'user_profile/login.html', {'form': form, 'show_navbar': False})
