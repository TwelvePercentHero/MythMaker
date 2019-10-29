from django.conf import settings
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from accounts.models import MythMakerMembership

from .models import Audio
from .forms import AudioUpload

def audio(request, audio_id):
    audio = Audio.objects.get(pk = audio_id)
    context = {'audio': audio}
    return render(request, 'audio/audio.html', context)

def audiolist(request):
    user = request.user
    if request.user.is_authenticated:
        mythmaker_membership = MythMakerMembership.objects.get(user = user)
    else:
        mythmaker_membership = None
    audios = Audio.objects.all().order_by('title')
    context = {'audios' : audios, 'mythmaker_membership' : mythmaker_membership}
    return render(request, 'audio/audiolist.html', context)
