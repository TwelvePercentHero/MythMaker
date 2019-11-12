from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User

class Audio(models.Model):
    title = models.CharField(max_length = 100)
    creator = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)
    date_posted = models.DateTimeField(auto_now_add = True)
    description = models.CharField(max_length = 250)
    audio_file = models.FileField(
        upload_to = 'audio',
        validators = [FileExtensionValidator(allowed_extensions = ['wav', 'aiff', 'mp3'])],
        blank = False)
    cover_image = models.ImageField(upload_to = 'audio_covers', blank = True)
    audio_thumbnail = models.ImageField(upload_to = 'audio_thumbnails', blank = True)
    audio_likes = models.IntegerField(default = 0)
    audio_comment_count = models.IntegerField(default = 0)

    class Meta:
        verbose_name = 'Audio'
        verbose_name_plural = 'Audios'

    def __str__(self):
        return self.title
