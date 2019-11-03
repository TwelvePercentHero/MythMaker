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

def searchresults(request):
    videos = Video.objects.filter(Q(title__icontains = request.GET['q']) | Q(description__icontains = request.GET['q']))
    stories = Story.objects.filter(Q(title__icontains = request.GET['q']) | Q(synopsis__icontains = request.GET['q']))
    audios = Audio.objects.filter(Q(title__icontains = request.GET['q']) | Q(description__icontains = request.GET['q']))
    mythmakers = User.objects.filter(Q(username__icontains = request.GET['q']))
    context = {'videos' : videos, 'stories' : stories, 'audios' : audios, 'mythmakers' : mythmakers}
    return render(request, 'main/searchresults.html', context)