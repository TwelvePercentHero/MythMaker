from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import ExtendedAuthForm

urlpatterns = [
    path('register/', views.register, name='register'),
    path('activate/(<uidb64>[0-9A-Za-z_\-]+)/(<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/', views.activate, name='activate'),
    path('profile/', views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html', authentication_form=ExtendedAuthForm)),
    path('logout/', auth_views.LogoutView.as_view(), name='logout')
]