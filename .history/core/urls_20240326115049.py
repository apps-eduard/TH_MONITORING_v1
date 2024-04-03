from django.contrib import admin
from django.urls import path, include
from user_profile.views import login_view
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view, name='login'),
    path('th_monitoring/', include('th_monitoring.urls', namespace='th_monitoring')),
    path('user_profile/', include('user_profile.urls')),
    path('logout/', LogoutView.as_view(next_page='user_profilelogin'), name='logout'),

]
