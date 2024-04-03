# core/urls.py
from django.contrib import admin
from django.urls import path, include  # include is needed to reference app-specific urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('th_monitoring/', include('th_monitoring.urls')),
    # Add other app urls here as needed
]
