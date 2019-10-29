from django.urls import path

from . import views

urlpatterns = [
    path('audio/<int:audio_id>', views.audio, name='audio'),
]