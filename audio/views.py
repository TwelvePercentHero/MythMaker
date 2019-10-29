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
