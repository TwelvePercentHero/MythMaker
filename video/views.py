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
    video_list = Video.objects.all().order_by('title')
    videos = Paginator(video_list, 3)
    grouped_videos = []
    for page in videos.page_range:
        page_objects = videos.page(page).object_list
        grouped_videos.append(page_objects)
    context = {'videos' : videos, 'grouped_videos' : grouped_videos}
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
            return redirect(reverse('profile'))


