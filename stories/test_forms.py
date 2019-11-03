from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from .forms import StoryUpload

testfile = (
    b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x00\x00\x00\x21\xf9\x04'
    b'\x01\x0a\x00\x01\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02'
    b'\x02\x4c\x01\x00\x3b'
    )

class TestStoryForm(TestCase):

    def test_story_upload_with_images(self):
        form = StoryUpload({
            'title' : 'Test Title',
            'synopsis' : 'Test Synopsis',
            'story' : 'This is a test story',
            'cover_image' : SimpleUploadedFile('small.gif', testfile, content_type = 'image/gif'),
            'story_thumbnail' : SimpleUploadedFile('small.gif', testfile, content_type = 'image/gif')
            })
        self.assertTrue(form.is_valid)
    
    def test_story_upload_without_images(self):
        form = StoryUpload({'title' : 'Test Title',
                            'synopsis' : 'Test Synopsis',
                            'story' : 'This is a test story'})
        self.assertTrue(form.is_valid)