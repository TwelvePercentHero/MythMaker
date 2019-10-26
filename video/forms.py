from django import forms
from django.forms import ModelForm

from .models import Video

class VideoUpload(ModelForm):
    title = forms.CharField(required = True)
    video_file = forms.FileField(required = False, label = 'video_file')
    thumbnail = forms.ImageField(required = False, label = 'thumbnail')
    description = forms.CharField(required = True)

    class Meta:
        model = Video
        fields = ('title', 'video_file', 'thumbnail', 'description')

    def clean_video_upload(self):
        title = self.cleaned_data['title']
        video_file = self.cleaned_data['video_file']
        thumbnail = self.cleaned_data['thumbnail']
        description = self.cleaned_data['description']

        return clean_video_upload