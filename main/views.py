from django.shortcuts import render
from video.models import Video
from stories.models import Story

def index(request):
    latest_videos = Video.objects.order_by('date_posted')[0:5]
    latest_stories = Story.objects.order_by('date_posted')[0:5]
    context = {'latest_videos' : latest_videos, 'latest_stories' : latest_stories}
    return render(request, 'main/index.html', context)