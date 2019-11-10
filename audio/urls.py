from django.urls import path

from . import views

urlpatterns = [
    path('audio/<int:audio_id>', views.audio, name='audio'),
    path('audiolist/', views.audiolist, name='audiolist'),
    path('uploadaudio/', views.uploadaudio, name='uploadaudio'),
    path('deleteaudio/<int:audio_id>', views.deleteaudio, name = 'deleteaudio'),
]