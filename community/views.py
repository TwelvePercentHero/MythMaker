from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import Like

from stories.models import Story
from video.models import Video
from audio.models import Audio


@login_required
def like_story(request, story_id):
    user = request.user
    story = Story.objects.get(pk = story_id)
    context = {'user' : user, 'story' : story}
    if request.method == 'POST':
        if not Like.objects.filter(liked_by = user, story = story).exists():
            new_like = Like(liked_by = user, story_type = 'STORY', story = story)
            new_like.save()
            story.story_likes += 1
            story.save()
            messages.success(request, 'Story liked!')
            return redirect(reverse('story', kwargs = {'story_id' : story_id}))
        else:
            messages.warning(request, 'You have already liked this story!')
            return redirect(reverse('story', kwargs = {'story_id': story_id}))

@login_required
def like_video(request, video_id):
    user = request.user
    video = Video.objects.get(pk = video_id)
    context = {'user' : user, 'video' : video}
    if request.method == 'POST':
        if not Like.objects.filter(liked_by = user, video = video).exists():
            new_like = Like(liked_by = user, story_type = 'VIDEO', video = video)
            new_like.save()
            video.video_likes += 1
            video.save()
            messages.success(request, 'Video liked!')
            return redirect(reverse('video', kwargs = {'video_id' : video_id}))
        else:
            messages.warning(request, 'You have already liked this video!')
            return redirect(reverse('video', kwargs = {'video_id' : video_id}))

@login_required
def like_audio(request, audio_id):
    user = request.user
    audio = Audio.objects.get(pk = audio_id)
    context = {'user' : user, 'audio': audio}
    if request.method == 'POST':
        if not Like.objects.filter(liked_by = user, audio = audio).exists():
            new_like = Like(liked_by = user, story_type = 'AUDIO', audio = audio)
            new_like.save()
            audio.audio_likes += 1
            audio.save()
            messages.success(request, 'Audio liked!')
            return redirect(reverse('audio', kwargs = {'audio_id' : audio_id}))
        else:
            messages.warning(request, 'You have already liked this audio!')
            return redirect(reverse('audio', kwargs = {'audio_id' : audio_id}))

