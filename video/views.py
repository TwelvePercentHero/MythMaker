from django.shortcuts import render
from .models import Video

def video(request, video_id):
    video = Video.objects.get(pk = video_id)
    context = {'video' : video}
    return render(request, 'video/video.html', context)
