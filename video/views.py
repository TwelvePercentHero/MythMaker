from django.conf import settings
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from accounts.views import get_user_membership
from accounts.models import MythMaker, Membership, MythMakerMembership, Subscription

from .models import Video
from .forms import VideoUpload

def video(request, video_id):
    video = Video.objects.get(pk = video_id)
    context = {'video' : video}
    return render(request, 'video/video.html', context)

def videolist(request):
    user = request.user
    if request.user.is_authenticated:
        mythmaker_membership = MythMakerMembership.objects.get(user = user)
    else:
        mythmaker_membership = None
    videos = Video.objects.all().order_by('title')
    context = {'videos' : videos, 'mythmaker_membership' : mythmaker_membership}
    return render(request, 'video/videolist.html', context)

@login_required
def uploadvideo(request):
    user = request.user
    mythmaker_membership = MythMakerMembership.objects.get(user = user)
    if request.method == 'POST':
        form = VideoUpload(request.POST, request.FILES)
        if form.is_valid():
            form.instance.uploaded_by = request.user
            form.save(commit = True)
            return redirect(reverse('videolist'))
    else:
        # Only Premium members can upload videos
        if mythmaker_membership.membership_id == 2:
            form = VideoUpload()
            return render(request, 'video/uploadvideo.html', {'form' : form})
        else:
            return render(request, 'main/premium.html')


