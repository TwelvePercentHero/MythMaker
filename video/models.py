from django.db import models
from django.contrib.auth.models import User

class Video(models.Model):
    title = models.CharField(max_length = 100)
    uploaded_by = models.OneToOneField(User, on_delete = models.CASCADE, blank = True, null = True)
    date_posted = models.DateTimeField(auto_now_add = True)
    video_file = models.FileField(upload_to = 'videos')
    thumbnail = models.FileField(upload_to = 'thumbnails')

    def __str__(self):
        return self.title
