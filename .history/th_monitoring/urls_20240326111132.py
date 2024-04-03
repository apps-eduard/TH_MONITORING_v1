from django.urls import path
from .views import monitoring_dashboard

urlpatterns = [
    path('', monitoring_dashboard, name='dashboard'),  # The name 'index' is used here
]
