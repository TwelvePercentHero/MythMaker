from django.urls import path

from . import views

urlpatterns = [
    path('like_story/<int:story_id>', views.like_story, name='like_story'),
]