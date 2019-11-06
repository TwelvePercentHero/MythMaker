from django.db import models
from django.contrib.auth.models import User
from tinymce import models as tinymce_models

class Story(models.Model):
    title = models.CharField(max_length = 100)
    author = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)
    date_posted = models.DateTimeField(auto_now_add = True)
    synopsis = models.CharField(max_length = 250)
    story = tinymce_models.HTMLField(max_length = 10000, blank = True, null = True)
    cover_image = models.ImageField(upload_to = 'cover_images', blank = True)
    story_thumbnail = models.ImageField(upload_to = 'story_thumbnails', blank = True)
    story_likes = models.IntegerField(default = 0)

    class Meta:
        verbose_name = 'Story'
        verbose_name_plural = 'Stories'

    def __str__(self):
        return self.title