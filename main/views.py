from django.shortcuts import render
from video.models import Video

def index(request):
    latest_videos = Video.objects.order_by('date_posted')[0:5]
    context = {'latest_videos' : latest_videos}
    return render(request, 'main/index.html', context)
