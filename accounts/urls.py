from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
from .forms import ExtendedAuthForm

urlpatterns = [
    path('userlist/', views.userlist, name='userlist'),
    path('user/<int:user_id>', views.publicprofile, name='publicprofile'),
    path('register/', views.register, name='register'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('profile/', views.profile, name='profile'),
    path('edit/', views.edit, name='edit'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html',
                                                authentication_form=ExtendedAuthForm)),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/reset.html',
                                                                 html_email_template_name='registration/reset_email.html',
                                                                 subject_template_name='registration/reset_subject.txt',
                                                                 success_url='sent'),
                                                                 name='reset'),
    path('password_reset/sent/', auth_views.PasswordResetDoneView.as_view(template_name='registration/reset_sent.html'),
                                                                        name='reset_sent'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/reset_confirm.html'),
                                                                                name='reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/reset_done.html'),
                                                                     name='reset_done'),
    path('benefits/', views.benefits, name='benefits'),
    path('upgrade/', views.upgrade, name='upgrade'),
    path('update_membership/<subscription_id>/', views.update, name='update_membership'),
    path('confirm_cancel/', views.confirm_cancel, name='confirm_cancel'),
    path('cancel/', views.cancel, name='cancel'),
]