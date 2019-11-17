from django.test import TestCase
from .models import Video

class TestVideoModel(TestCase):

    def test_title_is_a_string(self):
        video = Video(title = 'Test Video Title')
        self.assertEqual(video.title, str(video))

    def test_verbose_name_plural(self):
        self.assertEqual(str(Video._meta.verbose_name_plural), 'Videos')