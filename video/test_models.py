from django.test import TestCase
from .models import Video

class TestVideoModel(TestCase):

    def test_title_is_a_string(self):
        video = Video(title = 'Test Video Title')
        self.assertEqual(video.title, str(video))