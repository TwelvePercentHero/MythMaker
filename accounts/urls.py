from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
from .forms import ExtendedAuthForm

urlpatterns = [
    path('register/', views.register, name='register'),
    path('activate/(<uidb64>[0-9A-Za-z_\-]+)/(<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/', views.activate, name='activate'),
    path('profile/', views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html',
                                                authentication_form=ExtendedAuthForm)),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html',
                                                                 html_email_template_name='registration/reset_email.html',
                                                                 subject_template_name='registration/reset_subject.txt',
                                                                 success_url='sent'),
                                                                 name='reset'),
    path('password_reset/sent/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_sent.html'),
                                                                        name='reset_sent'),
    path('password_reset_confirm/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),
                                                                                name='reset_confirm')
]