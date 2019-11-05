from django.db import models
from django.contrib.auth.models import User

from stories.models import Story
from video.models import Video
from audio.models import Audio

class Like(models.Model):
    liked_by = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)
    liked_story = models.ForeignKey(Story, on_delete = models.CASCADE, blank = True, null = True)
    liked_video = models.ForeignKey(Video, on_delete = models.CASCADE, blank = True, null = True)
    liked_audio = models.ForeignKey(Audio, on_delete = models.CASCADE, blank = True, null = True)
    created = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name = 'Like'
        verbose_name_plural = 'Likes'

    def __str__(self):
        return self.liked_by.username

class Comment(models.Model):
    commenter = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)
    story = models.ForeignKey(Story, on_delete = models.CASCADE, blank = True, null = True)
    video = models.ForeignKey(Video, on_delete = models.CASCADE, blank = True, null = True)
    audio = models.ForeignKey(Audio, on_delete = models.CASCADE, blank = True, null = True)
    created = models.DateTimeField(auto_now_add = True)
    comment = models.CharField(max_length = 500)

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return self.commenter.username
    