from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth.models import User
from itertools import chain
from video.models import Video
from stories.models import Story
from audio.models import Audio

def index(request):
    latest_videos = Video.objects.order_by('date_posted')[0:5]
    latest_stories = Story.objects.order_by('date_posted')[0:5]
    latest_audio = Audio.objects.order_by('date_posted')[0:5]
    context = {'latest_videos' : latest_videos, 'latest_stories' : latest_stories, 'latest_audio' : latest_audio}
    return render(request, 'main/index.html', context)

'''def searchresults(request):
    videos = Video.objects.filter()
    stories = Story.objects.filter()
    audio = Audio.objects.filter()
    mythmakers = Users.objects.filter()'''