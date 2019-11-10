from django.conf import settings
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from accounts.models import MythMakerMembership

from .models import Audio
from .forms import AudioUpload

from community.models import Comment
from community.forms import CommentUpload

def audio(request, audio_id):
    user = request.user
    audio = Audio.objects.get(pk = audio_id)
    comments = Comment.objects.filter(audio = audio).order_by('created')
    if user.is_authenticated:
        if request.method == 'POST':
            form = CommentUpload(request.POST)
            if form.is_valid():
                form.instance.commenter = user
                form.instance.audio = audio
                form.save()
                audio.audio_comment_count += 1
                audio.save()
                return redirect(reverse('audio', kwargs = {'audio_id' : audio_id}))
        else:
            form = CommentUpload()
            context = {'user' : user, 'audio' : audio, 'comments' : comments, 'form' : form}
            return render(request, 'audio/audio.html', context)
    context = {'user' : user, 'audio': audio, 'comments' : comments}
    return render(request, 'audio/audio.html', context)

def audiolist(request):
    user = request.user
    if request.user.is_authenticated:
        mythmaker_membership = MythMakerMembership.objects.get(user = user)
    else:
        mythmaker_membership = None
    audios = Audio.objects.all().order_by('title')
    audio_count = audios.count()
    page = request.GET.get('page', 1)
    paginated_list = Paginator(audios, 5)
    try:
        audiolist = paginated_list.page(page)
    except PageNotAnInteger:
        audiolist = paginated_list.page(1)
    except EmptyPage:
        audiolist = paginated_list.page(paginator.num_pages)
    context = {'user' : user, 'audio_count' : audio_count, 'audiolist' : audiolist, 'mythmaker_membership' : mythmaker_membership}
    return render(request, 'audio/audiolist.html', context)

@login_required
def uploadaudio(request):
    user = request.user
    mythmaker_membership = MythMakerMembership.objects.get(user = user)
    if request.method == 'POST':
        form = AudioUpload(request.POST, request.FILES)
        if form.is_valid():
            form.instance.creator = request.user
            form.save(commit = True)
            return redirect(reverse('audiolist'))
    else:
        # Only Premium members can upload audio
        if mythmaker_membership.membership_id == 2:
            form = AudioUpload()
            return render(request, 'audio/uploadaudio.html', {'form' : form})
        else:
            return render(request, 'main/premium.html')

@login_required
def deleteaudio(request, audio_id):
    user = request.user
    audio = Audio.objects.get(pk = audio_id)
    if request.method == 'POST':
        if user == audio.creator:
            audio.delete()
            return redirect(reverse('audiolist'))
        else:
            return redirect(reverse('audiolist'))
