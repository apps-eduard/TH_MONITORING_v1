from django.urls import path
from .views import login_view, logout_view, register

from .views import register

app_name = 'user_profile'  # This is the namespace for the URLs in this app

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout_view, name='logout'),
    path('edit-profile/', views.edit_profile_view, name='edit_profile'),


]
