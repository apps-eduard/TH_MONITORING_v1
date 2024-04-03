from django.urls import path
from .views import login_view, profile_view
from .views import logout_view
from .views import register

app_name = 'user_profile'  # This is the namespace for the URLs in this app

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register, name='register'),
    path('profile/', profile_view, name='profile'),  # Ensure this is in place if you haven't added it yet
    path('logout/', logout_view, name='logout'),


]
