from django.urls import path

from . import views

urlpatterns = [
    path('like_story/<int:story_id>', views.like_story, name = 'like_story'),
    path('like_video/<int:video_id>', views.like_video, name = 'like_video'),
    path('like_audio/<int:audio_id>', views.like_audio, name = 'like_audio'),
    path('story_comment/<int:story_id>', views.story_comment, name = 'story_comment'),
]