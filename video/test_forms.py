from django.test import TestCase
from django.core.files import File
from django.core.files.uploadedfile import SimpleUploadedFile
from .forms import VideoUpload

testimage = (
    b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x00\x00\x00\x21\xf9\x04'
    b'\x01\x0a\x00\x01\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02'
    b'\x02\x4c\x01\x00\x3b'
)

class TestVideoForm(TestCase):

    def test_video_upload_with_images(self):
        form = VideoUpload({
            'title' : 'Test Video Title',
            'description' : 'Test Video Description',
            'thumbnail' : SimpleUploadedFile('small.gif', testimage, content_type = 'image/gif'),
            'video_file' : File(open('media/videos/earth_video.mp4'))
        })
        self.assertTrue(form.is_valid)

