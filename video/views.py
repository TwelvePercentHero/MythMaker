from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Video

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
