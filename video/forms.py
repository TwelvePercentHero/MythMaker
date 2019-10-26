from django import forms
from django.forms import ModelForm

from .models import Video

class VideoUpload(ModelForm):
    title = forms.CharField(required = True)
    video_file = forms.FileField(required = True)
    thumbnail = forms.ImageField(required = True)

    class Meta:
        model = Video
        fields = ('title', 'video_file', 'thumbnail')


    def clean_video_upload(self):
        title = self.cleaned_data['title']
        video_file = self.cleaned_data['video_file']
        thumbnail = self.cleaned_data['thumbnail']

        return clean_video_upload