from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from .models import Video
from accounts.models import Membership
from video.views import videolist

class TestVideoViews(TestCase):

    def test_videolist(self):
        user = User.objects.create_user(
            username = 'TestUser',
            email = 'test@test.com',
            password = 'testpassword'
        )
        membership = Membership.objects.create(
            membership_type = 'FR',
            id = '1'
        )
        page = self.client.get('/videolist/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'video/videolist.html')


    def test_video(self):
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
        page = self.client.get('/video/{}'.format(video.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'video/video.html')
        
