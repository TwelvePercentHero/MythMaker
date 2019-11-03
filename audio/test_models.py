from django.test import TestCase
from .models import Audio

class TestAudioModel(TestCase):

    def test_title_is_a_string(self):
        audio = Audio(title = 'Test Audio Title')
        self.assertEqual(audio.title, str(audio))