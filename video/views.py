from django.conf import settings
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.decorators import login_required

from accounts.models import MythMakerMembership

from .models import Video
from .forms import VideoUpload

from community.models import Comment
from community.forms import CommentUpload

def video(request, video_id):
    user = request.user
    video = Video.objects.get(pk = video_id)
    comments = Comment.objects.filter(video = video).order_by('created')
    comments_count = comments.count()
    more_videos = Video.objects.filter(uploaded_by = video.uploaded_by).order_by('-video_likes')[0:5]
    if user.is_authenticated:
        if request.method == 'POST':
            form = CommentUpload(request.POST)
            if form.is_valid():
                form.instance.commenter = user
                form.instance.video = video
                form.save()
                video.video_comment_count += 1
                video.save()
                messages.success(request, 'Your comment was successfully published!')
                return redirect(reverse('video', kwargs = {'video_id' : video_id}))
        else:
            form = CommentUpload()
            context = {
                'user' : user,
                'video' : video,
                'comments' : comments,
                'comments_count' : comments_count,
                'more_videos' : more_videos,
                'form' : form}
            return render(request, 'video/video.html', context)
    context = {
        'user' : user,
        'video' : video,
        'comments' : comments,
        'comments_count' : comments_count,
        'more_videos' : more_videos,
        }
    return render(request, 'video/video.html', context)

def videolist(request):
    user = request.user
    if request.user.is_authenticated:
        mythmaker_membership = MythMakerMembership.objects.get(user = user)
    else:
        mythmaker_membership = None
    videos = Video.objects.all().order_by('title')
    video_count = videos.count()
    page = request.GET.get('page', 1)
    paginated_list = Paginator(videos, 5)
    try:
        videolist = paginated_list.page(page)
    except PageNotAnInteger:
        videolist = paginated_list.page(1)
    except EmptyPage:
        videolist = paginated_list.page(paginator.num_pages)
    context = {'user' : user, 'video_count' : video_count, 'videolist' : videolist, 'mythmaker_membership' : mythmaker_membership}
    return render(request, 'video/videolist.html', context)

@login_required
def uploadvideo(request):
    user = request.user
    mythmaker_membership = MythMakerMembership.objects.get(user = user)
    if request.method == 'POST':
        form = VideoUpload(request.POST, request.FILES)
        if form.is_valid():
            form.instance.uploaded_by = request.user
            video = form.save(commit = True)
            messages.success(request, 'You have successfully published your video!')
            return redirect(reverse('video', kwargs = {'video_id' : video.id}))
    else:
        # Only Premium members can upload videos
        if mythmaker_membership.membership_id == 2:
            form = VideoUpload()
            return render(request, 'video/uploadvideo.html', {'form' : form})
        else:
            return render(request, 'main/premium.html')

@login_required
def deletevideo(request, video_id):
    user = request.user
    video = Video.objects.get(pk = video_id)
    if request.method == 'POST':
        if user == video.uploaded_by:
            video.delete()
            messages.success(request, 'Your video was successfully deleted.')
            return redirect(reverse('videolist'))
        else:
            messages.warning(request, 'You do not have permission to do that.')
            return redirect(reverse('videolist'))


