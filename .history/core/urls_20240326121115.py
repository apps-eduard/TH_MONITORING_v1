from django.contrib import admin
from django.urls import path, include
from user_profile.views import login_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view, name='login'),
    path('th_monitoring/', include('th_monitoring.urls', namespace='th_monitoring')),
        path('user_profile/', include('user_profile.urls')),

]
