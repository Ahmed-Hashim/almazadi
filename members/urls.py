
from django.urls import path
from . views import PasswordsChangeView
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [

    path('login_user', views.login_user,name='login'),
    path('logout_user', views.logout_user,name='logout'),
    path('profile', views.profile,name='profile'),
    path('settings', views.settings,name='settings'),
    #path('change_password', auth_views.PasswordChangeView.as_view(template_name='registration/change_password.html')),
    path('change_password', PasswordsChangeView.as_view(template_name='registration/change_password.html')),
    
    ]