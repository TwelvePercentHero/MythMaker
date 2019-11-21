from django.test import TestCase
from django.contrib.auth.models import User
from .models import Like
from .views import like_story, like_video, like_audio
from accounts.models import Membership
from stories.models import Story
from video.models import Video
from audio.models import Audio

class TestCommunityViews(TestCase):

    def test_story_like_count(self):
        user = User.objects.create_user(
            username = 'TestUser',
            email = 'test@test.com',
            password = 'testpassword'
        )
        membership = Membership.objects.create(
            membership_type = 'FR',
            id = '1'
        )
        story = Story.objects.create(
            title = 'Test Story',
            author = user,
            synopsis = 'This is a Test Synopsis for the Test Story',
            story = 'This is a Test Story for the Test Story',
            cover_image = 'media/cover_images/test-header.jpg',
            story_thumbnail = 'media/thumbnails/test-thumb-1.jpg'
        )
        self.client.login(username = 'TestUser', password = 'testpassword')
        page = self.client.post('/like_story/{}'.format(story.id))
        story_like = Story.objects.get(title = 'Test Story').story_likes
        self.assertEqual(story_like, 1)

    def test_video_like_count(self):
        user = User.objects.create_user(
            username = 'TestUser',
            email = 'test@test.com',
            password = 'testpassword'
        )
        membership = Membership.objects.create(
            membership_type = 'FR',
            id = '1'
        )
        video = Video.objects.create(
            title = 'Test Video',
            video_file = 'media/video/test-video-1.mp4',
            description = 'This is a Test Description for the Test Video',
            thumbnail = 'media/thumbnails/test-thumb-1.jpg',
            uploaded_by = user
        )
        self.client.login(username = 'TestUser', password = 'testpassword')
        page = self.client.post('/like_video/{}'.format(video.id))
        video_like = Video.objects.get(title = 'Test Video').video_likes
        self.assertEqual(video_like, 1)

    def test_audio_like_count(self):
        user = User.objects.create_user(
            username = 'TestUser',
            email = 'test@test.com',
            password = 'testpassword'
        )
        membership = Membership.objects.create(
            membership_type = 'FR',
            id = '1'
        )
        audio = Audio.objects.create(
            title = 'Test Audio',
            description = 'This is a Test Description for the Test Audio',
            audio_file = 'media/audio/test_audio_file.mp3',
            cover_image = 'media/cover_images/test-header.jpg',
            audio_thumbnail = 'media/thumbnails/test-thumb-1.jpg',
            creator = user
        )
        self.client.login(username = 'TestUser', password = 'testpassword')
        page = self.client.post('/like_audio/{}'.format(audio.id))
        audio_like = Audio.objects.get(title = 'Test Audio').audio_likes
        self.assertEqual(audio_like, 1)