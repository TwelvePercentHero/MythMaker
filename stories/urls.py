from django.urls import path

from . import views

urlpatterns = [
    path('story/<int:story_id>', views.story, name = 'story'),
    path('storylist/', views.storylist, name = 'storylist'),
    path('uploadstory/', views.uploadstory, name = 'uploadstory'),
    path('deletestory/<int:story_id>', views.deletestory, name = 'deletestory'),
]