from django import forms
from django.forms import ModelForm

from .models import Audio

class AudioUpload(ModelForm):
    title = forms.CharField(required = True)
    audio_file = forms.FileField(required = False, label = 'audio_file')
    audio_thumbnail = forms.ImageField(required = False, label = 'audio_thumbnail')
    cover_image = forms.ImageField(required = False, label = 'cover_image')
    description = forms.CharField(required = True)

    class Meta:
        model = Audio
        fields = ('title', 'audio_file', 'audio_thumbnail', 'cover_image', 'description')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class' : 'form-control', 'placeholder' : 'Enter audio title'})
        self.fields['description'].widget.attrs.update({'class' : 'form-control', 'placeholder' : 'Enter a description'})
        
    def clean_audio_upload(self):
        title = self.cleaned_data['title']
        audio_file = self.cleaned_data['audio_file']
        audio_thumbnail = self.cleaned_data['audio_thumbnail']
        cover_image = self.cleaned_data['cover_image']
        description = self.cleaned_data['description']

        return clean_audio_upload