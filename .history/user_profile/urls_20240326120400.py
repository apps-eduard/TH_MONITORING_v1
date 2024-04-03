from django.urls import path
from .views import login_view, profile_view
from .views import logout_view
from . import views


urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', views.register, name='register'),
    path('profile/', profile_view, name='profile'),  # Ensure this is in place if you haven't added it yet
    path('logout/', logout_view, name='logout'),

]
