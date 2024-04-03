from django.urls import path
from .views import monitoring_view

urlpatterns = [
        path('', views.your_view_name, name='index'),  # Replace your_view_name with your actual view function

]
