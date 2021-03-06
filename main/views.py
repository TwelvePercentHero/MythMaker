from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth.models import User
from accounts.models import MythMakerMembership
from video.models import Video
from stories.models import Story
from audio.models import Audio

def index(request):
    latest_videos = Video.objects.order_by('-date_posted')[0:5]
    latest_stories = Story.objects.order_by('-date_posted')[0:5]
    latest_audio = Audio.objects.order_by('-date_posted')[0:5]
    context = {
        'latest_videos' : latest_videos,
        'latest_stories' : latest_stories,
        'latest_audio' : latest_audio
        }
    return render(request, 'main/index.html', context)

def about(request):
    return render(request, 'main/about.html')

def searchresults(request):
    user = request.user
    if request.user.is_authenticated:
        mythmaker_membership = MythMakerMembership.objects.get(user = user)
    else:
        mythmaker_membership = None
    query = request.GET['q']
    videos = Video.objects.filter(Q(title__icontains = query) | Q(description__icontains = query))[0:5]
    stories = Story.objects.filter(Q(title__icontains = query) | Q(synopsis__icontains = query))[0:5]
    audios = Audio.objects.filter(Q(title__icontains = query) | Q(description__icontains = query))[0:5]
    mythmakers = User.objects.filter(Q(username__icontains = query))[0:5]
    context = {
        'user' : user,
        'mythmaker_membership' : mythmaker_membership,
        'query' : query,
        'videos' : videos,
        'stories' : stories,
        'audios' : audios,
        'mythmakers' : mythmakers
        }
    return render(request, 'main/searchresults.html', context)

def privacy(request):
    return render(request, 'main/privacy.html')

def handler404(request, exception):
    return render(request, 'main/404.html', status=404)

def handler500(request):
    return render(request, 'main/500.html', status=500)