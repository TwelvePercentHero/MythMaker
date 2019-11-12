from django import forms
from django.forms import ModelForm

from .models import Video

class VideoUpload(ModelForm):
    title = forms.CharField(required = True)
    video_file = forms.FileField(required = True, label = 'video_file')
    thumbnail = forms.ImageField(required = True, label = 'thumbnail')
    description = forms.CharField(required = True, widget = forms.Textarea(attrs={'rows': 10, 'cols': 20}))

    class Meta:
        model = Video
        fields = ('title', 'video_file', 'thumbnail', 'description')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class' : 'form-control', 'placeholder' : 'Enter a video title'})
        self.fields['description'].widget.attrs.update({'class' : 'form-control', 'placeholder' : 'Enter a description'})
        self.fields['video_file'].widget.attrs.update({'class' : 'form-control'})
        self.fields['thumbnail'].widget.attrs.update({'class' : 'form-control'})

    def clean_video_upload(self):
        title = self.cleaned_data['title']
        video_file = self.cleaned_data['video_file']
        thumbnail = self.cleaned_data['thumbnail']
        description = self.cleaned_data['description']

        return clean_video_upload