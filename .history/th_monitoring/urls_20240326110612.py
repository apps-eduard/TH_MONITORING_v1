from django.urls import path
from .views import monitoring_dashboard

urlpatterns = [
    path('', monitoring_view, name='index'),  # The name 'index' is used here
]
