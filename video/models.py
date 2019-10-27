from django.db import models
from django.db.models.signals import post_save
from django import forms
from django.contrib.auth.models import User
from django.conf import settings

class Video(models.Model):
    title = models.CharField(max_length = 100)
    uploaded_by = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)
    date_posted = models.DateTimeField(auto_now_add = True)
    video_file = models.FileField(upload_to = 'videos', blank = True)
    thumbnail = models.FileField(upload_to = 'thumbnails', blank = True, help_text = 'Recommended image size 1920x1080px')
    description = models.CharField(max_length = 1000, blank = True, null = True)

    def __str__(self):
        return self.title
