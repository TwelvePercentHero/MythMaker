from django.test import TestCase
from .models import Video

class TestVideoViews(TestCase):

    def test_videolist(self):
        page = self.client.get('/videolist/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'video/videolist.html')

    def test_video(self):
        video = Video(
            title = 'Test Video',
            video_file = 'media/video/test-video-1.mp4',
            description = 'This is a Test Description for the Test Video',
            thumbnail = 'media/thumbnails/test-thumb-1.jpg'
        )
        video.save()
        page = self.client.get('/video/{}'.format(video.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'video/video.html')
