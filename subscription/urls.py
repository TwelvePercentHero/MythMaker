from django.urls import path
from . import views

urlpatterns = [
    path('benefits/', views.benefits, name='benefits'),
]