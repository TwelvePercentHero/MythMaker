from django import forms
from django.forms import ModelForm

from .models import Story

class StoryUpload(ModelForm):
    title = forms.CharField(required = True)
    synopsis = forms.CharField(required = True)
    story = forms.CharField(required = True, widget = forms.Textarea(attrs={'rows': 100, 'cols': 80}))
    cover_image = forms.ImageField(required = False, label = 'cover-image')

    class Meta:
        model = Story
        fields = ('title', 'synopsis', 'story', 'cover_image')

    def clean_story_upload(self):
        title = self.cleaned_data['title']
        synopsis = self.cleaned_data['synopsis']
        story = self.cleaned_data['story']
        cover_image = self.cleaned_data['cover_image']

        return clean_story_upload