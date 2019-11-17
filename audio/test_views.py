from django.test import TestCase
from django.core.files import File
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Audio

testfile = (
    b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x00\x00\x00\x21\xf9\x04'
    b'\x01\x0a\x00\x01\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02'
    b'\x02\x4c\x01\x00\x3b'
    )

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
            cover_image = SimpleUploadedFile('small.gif', testfile, content_type = 'image/gif'),
            audio_thumbnail = SimpleUploadedFile('small.gif', testfile, content_type = 'image/gif')
        )
        audio.save()
        page = self.client.get('/audio/{}'.format(audio.id))
        self.assertEqual(page.status_code, 200)
