from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import Like, Comment
from stories.models import Story


@login_required
def like_story(request, story_id):
    user = request.user
    story = Story.objects.get(pk = story_id)
    context = {'story' : story}
    if request.method == 'POST':
        new_like = Like(liked_by = user, story_type = 'STORY', story = story)
        new_like.save()
        return redirect(reverse('story', kwargs={'story_id' : story_id}))

