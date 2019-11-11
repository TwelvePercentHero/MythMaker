from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Story
from .forms import StoryUpload

from community.models import Comment
from community.forms import CommentUpload

def story(request, story_id):
    user = request.user
    story = Story.objects.get(pk = story_id)
    comments = Comment.objects.filter(story = story).order_by('created')
    comments_count = comments.count()
    more_stories = Story.objects.filter(author = story.author).order_by('-story_likes')[0:5]
    if user.is_authenticated:
        if request.method == 'POST':
            form = CommentUpload(request.POST)
            if form.is_valid():
                form.instance.commenter = user
                form.instance.story = story
                form.save()
                story.story_comment_count += 1
                story.save()
                messages.success(request, 'Your comment was successfully published!')
                return redirect(reverse('story', kwargs = {'story_id' : story_id}))
        else:
            form = CommentUpload()
            context = {
                'user' : user,
                'story' : story,
                'comments' : comments,
                'comments_count' : comments_count,
                'more_stories' : more_stories,
                'form' : form
                }
            return render(request, 'stories/story.html', context)
    context = {
        'user' : user,
        'story' : story,
        'comments' : comments,
        'comments_count' : comments_count,
        'more_stories' : more_stories
        }
    return render(request, 'stories/story.html', context)

def storylist(request):
    user = request.user
    stories = Story.objects.all().order_by('title')
    story_count = stories.count()
    page = request.GET.get('page', 1)
    paginated_list = Paginator(stories, 5)
    try:
        storylist = paginated_list.page(page)
    except PageNotAnInteger:
        storylist = paginated_list.page(1)
    except EmptyPage:
        storylist = paginated_list.page(paginator.num_pages)
    context = {
        'user' : user,
        'story_count' : story_count,
        'storylist' : storylist
        }
    return render(request, 'stories/storylist.html', context)

@login_required
def uploadstory(request):
    user = request.user
    if request.method == 'POST':
        form = StoryUpload(request.POST, request.FILES)
        if form.is_valid():
            form.instance.author = request.user
            story = form.save(commit = True)
            messages.success(request, 'You have successfully published your story!')
            return redirect(reverse('story', kwargs = {'story_id' : story.id}))
    else:
        form = StoryUpload()
        return render(request, 'stories/uploadstory.html', {'form' : form})

@login_required
def deletestory(request, story_id):
    user = request.user
    story = Story.objects.get(pk = story_id)
    if request.method == 'POST':
        if user == story.author:
            story.delete()
            messages.success(request, 'Your story was successfully deleted.')
            return redirect(reverse('storylist'))
        else:
            messages.warning(request, 'You do not have permission to do that.')
            return redirect(reverse('storylist'))
