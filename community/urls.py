from django.urls import path

from . import views

urlpatterns = [
    path('like_story/<int:story_id>', views.like_story, name = 'like_story'),
    path('like_video/<int:video_id>', views.like_video, name = 'like_video'),
]