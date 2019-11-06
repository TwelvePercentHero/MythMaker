from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import Story
from .forms import StoryUpload

from community.models import Like
from community.forms import CommentUpload

def story(request, story_id):
    user = request.user
    story = Story.objects.get(pk = story_id)
    if user.is_authenticated:
        if request.method == 'POST':
            form = CommentUpload(request.POST)
            if form.is_valid():
                form.instance.commenter = user
                Comment.story = story
                form.save()
                return redirect(reverse('story', kwargs = {'story_id' : story_id}))
        else:
            form = CommentUpload()
            context = {'user' : user, 'story' : story, 'form' : form}
            return render(request, 'stories/story.html', context)
    context = {'user' : user, 'story' : story}
    return render(request, 'stories/story.html', context)

def storylist(request):
    user = request.user
    stories = Story.objects.all().order_by('title')
    context = {'user' : user, 'stories' : stories}
    return render(request, 'stories/storylist.html', context)

@login_required
def uploadstory(request):
    user = request.user
    if request.method == 'POST':
        form = StoryUpload(request.POST, request.FILES)
        if form.is_valid():
            form.instance.author = request.user
            form.save(commit = True)
            return redirect(reverse('storylist'))
    else:
        form = StoryUpload()
        return render(request, 'stories/uploadstory.html', {'form' : form})
