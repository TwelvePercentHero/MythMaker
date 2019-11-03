from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth.models import User
from itertools import chain
from accounts.models import MythMakerMembership
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
    user = request.user
    if request.user.is_authenticated:
        mythmaker_membership = MythMakerMembership.objects.get(user = user)
    else:
        mythmaker_membership = None
    query = request.GET['q']
    videos = Video.objects.filter(Q(title__icontains = query) | Q(description__icontains = query))
    stories = Story.objects.filter(Q(title__icontains = query) | Q(synopsis__icontains = query))
    audios = Audio.objects.filter(Q(title__icontains = query) | Q(description__icontains = query))
    mythmakers = User.objects.filter(Q(username__icontains = query))
    context = {'user' : user, 'mythmaker_membership' : mythmaker_membership, 'query' : query, 'videos' : videos, 'stories' : stories, 'audios' : audios, 'mythmakers' : mythmakers}
    return render(request, 'main/searchresults.html', context)