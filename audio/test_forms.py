from django.test import TestCase
from django.core.files import File
from django.core.files.uploadedfile import SimpleUploadedFile
from .forms import AudioUpload

testimage = (
    b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x00\x00\x00\x21\xf9\x04'
    b'\x01\x0a\x00\x01\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02'
    b'\x02\x4c\x01\x00\x3b'
    )

class TestAudioForm(TestCase):

    def test_audio_upload_with_images(self):
        form = AudioUpload({
            'title' : 'Test Title',
            'description' : 'Test Audio Description',
            'audio_thumbnail' : SimpleUploadedFile('small.gif', testimage, content_type = 'image/gif'),
            'cover_image' : SimpleUploadedFile('small.gif', testimage, content_type = 'image/gif'),
            'audio_file' : File(open('media/audio/test_audio_file.mp3'))
            })
        self.assertTrue(form.is_valid)