from django import forms
from django.forms import ModelForm

from .models import Comment

class CommentUpload(ModelForm):
    comment = forms.CharField(required = True, widget = forms.Textarea(attrs={'rows': 5, 'cols': 50}))

    class Meta:
        model = Comment
        fields = ('comment',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['comment'].widget.attrs.update({'class' : 'form-control', 'placeholder' : 'Leave a Comment'})

    def clean_comment_upload(self):
        comment = self.cleaned_data['comment']

        return clean_comment_upload