from django.test import TestCase
from .models import Audio

class TestAudioViews(TestCase):

    def test_audiolist(self):
        page = self.client.get('/audiolist/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'audio/audiolist.html')

    def test_audio(self):
        audio = Audio(
            title = 'Test Audio',
            description = 'This is a Test Description for the Test Audio',
            audio_file = 'media/audio/test_audio_file.mp3',
            cover_image = 'media/cover_images/test-header.jpg',
            audio_thumbnail = 'media/thumbnails/test-thumb-1.jpg'
        )
        audio.save()
        page = self.client.get('/audio/{}'.format(audio.id))
        self.assertEqual(page.status_code, 200)
