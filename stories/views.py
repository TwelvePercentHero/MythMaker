from django.shortcuts import render
from django.contrib.auth.models import User

from .models import Story
from .forms import StoryUpload

def story(request, story_id):
    story = Story.objects.get(pk = story_id)
    context = {'story' : story}
    return render(request, 'stories/story.html', context)

def storylist(request):
    stories = Story.objects.all().order_by('title')
    context = {'stories' : stories}
    return render(request, 'stories/storylist.html', context)
