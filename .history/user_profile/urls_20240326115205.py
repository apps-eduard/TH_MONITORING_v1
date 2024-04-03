from django.urls import path
from .views import register_view, login_view, profile_view
from .views import 

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('profile/', profile_view, name='profile'),  # Ensure this is in place if you haven't added it yet
    path('logout/', logout_view, name='logout'),

]
