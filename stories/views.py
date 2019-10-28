from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

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
