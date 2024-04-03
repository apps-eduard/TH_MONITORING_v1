
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UserRegistrationForm
from django.contrib.auth.forms import AuthenticationForm

# You might want to pass context or user-specific data here
def profile_view(request):
    context = {'message': 'This is your profile page.'}
    return render(request, 'user_profile/profile.html', context)


from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.urls import reverse

def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to login page after successful registration
            return redirect('login')  # Using redirect with the name of the login url pattern
    else:
        form = UserRegistrationForm()
    return render(request, 'user_profile/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile')
    else:
        form = AuthenticationForm()
    return render(request, 'user_profile/login.html', {'form': form})
