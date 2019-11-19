from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from .models import Video
from accounts.models import Membership
from video.views import videolist

class TestVideoViews(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username = 'TestUser',
            email = 'test@test.com',
            password = 'testpassword'
        )
        test_membership = Membership.objects.create(
            membership_type = 'FR'
        )
        video = Video.objects.create(
            title = 'Test Video',
            video_file = 'media/video/test-video-1.mp4',
            description = 'This is a Test Description for the Test Video',
            thumbnail = 'media/thumbnails/test-thumb-1.jpg',
            uploaded_by = self.user
        )

    def test_videolist(self):
        request = self.factory.get('/videolist/')
        request.user = self.user
        response = videolist(request)        
        self.assertEqual(response.status_code, 200)

    def test_video(self):
        video = Video.objects.get(title = 'Test Video')
        response = self.client.get('/video/{}'.format(video.id))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'video/video.html')
        
