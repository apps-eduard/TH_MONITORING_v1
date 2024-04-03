# th_monitoring/urls.py

from django.urls import path
from . import views

app_name = 'th_monitoring'  # Define the app_name here

urlpatterns = [
    path('', views.monitoring_dashboard, name='dashboard'),
    # Add other paths as needed
]
