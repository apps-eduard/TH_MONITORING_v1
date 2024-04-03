# th_monitoring/urls.py

from django.urls import path
from . import views

app_name = 'th_monitoring'

urlpatterns = [
    path('', views.monitoring_dashboard, name='dashboard'),   
]
