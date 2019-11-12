from django import forms
from django.forms import ModelForm
from tinymce.widgets import TinyMCE

from .models import Story

class StoryUpload(ModelForm):
    title = forms.CharField(required = True, min_length = 5)
    synopsis = forms.CharField(required = True, min_length = 25)
    story = forms.CharField(required = True, min_length = 250, widget = TinyMCE(attrs={'rows': 10, 'cols': 60}))
    cover_image = forms.ImageField(required = True, label = 'cover-image')
    story_thumbnail = forms.ImageField(required = True, label = 'story_thumbnail')

    class Meta:
        model = Story
        fields = ('title', 'synopsis', 'story', 'cover_image', 'story_thumbnail')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class' : 'form-control'})
        self.fields['synopsis'].widget.attrs.update({'class' : 'form-control'})
        self.fields['story'].widget.attrs.update({'class' : 'form-control'})
        self.fields['cover_image'].widget.attrs.update({'class' : 'form-control'})
        self.fields['story_thumbnail'].widget.attrs.update({'class' : 'form-control'})

    def clean_story_upload(self):
        title = self.cleaned_data['title']
        synopsis = self.cleaned_data['synopsis']
        story = self.cleaned_data['story']
        cover_image = self.cleaned_data['cover_image']
        story_thumbnail = self.cleaned_data['story_thumbnail']

        return clean_story_upload