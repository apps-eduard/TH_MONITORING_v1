from django.shortcuts import render

def login_view(request):
    return render(request, 'login.html')

from django.shortcuts import render

# You might want to pass context or user-specific data here
def profile_view(request):
    context = {'message': 'This is your profile page.'}
    return render(request, 'user_profile/profile.html', context)
