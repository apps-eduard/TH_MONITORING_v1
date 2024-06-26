
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UserRegistrationForm, LoginForm
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm , UserEditForm
 
# @login_required
# def edit_profile_view(request):
#     if request.method == 'POST':
#         form = ProfileForm(request.POST, instance=request.user.profile)
#         if form.is_valid():
#             form.save()
#             return redirect('user_profile:profile')  # Redirect to profile page after successful edit
#     else:
#         form = ProfileForm(instance=request.user.profile)
    
#     return render(request, 'user_profile/edit_profile.html', {'form': form})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            # Redirect to user profile page or wherever you wish
            return redirect('/user/login/')  
    else:
        form = UserEditForm(instance=request.user)
    return render(request, 'user_profile/edit_user.html', {'form': form})


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
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, email=form.cleaned_data['email'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
            return redirect('th_monitoring:dashboard')
    else:
        form = LoginForm()
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
