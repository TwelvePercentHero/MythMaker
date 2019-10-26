from django.urls import path

from . import views

urlpatterns = [
    path('video/<int:video_id>', views.video, name='video'),
    path('videolist/', views.videolist, name='videolist'),
]