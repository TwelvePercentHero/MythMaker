from django.urls import path

from . import views

urlpatterns = [
    path('video/<int:video_id>', views.video, name='video'),
    path('videolist/', views.videolist, name='videolist'),
    path('uploadvideo/', views.uploadvideo, name='uploadvideo'),
    path('deletevideo/<int:video_id>', views.deletevideo, name='deletevideo'),
]