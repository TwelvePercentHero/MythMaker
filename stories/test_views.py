from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Story

testfile = (
    b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x00\x00\x00\x21\xf9\x04'
    b'\x01\x0a\x00\x01\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02'
    b'\x02\x4c\x01\x00\x3b'
    )

class TestStoryViews(TestCase):
    
    def test_storylist(self):
        page = self.client.get('/storylist/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'stories/storylist.html')

    def test_story(self):
        story = Story(
            title = 'Test Story',
            synopsis = 'Test synopsis',
            story = 'This is a Test Story',
            cover_image = SimpleUploadedFile('small.gif', testfile, content_type = 'image/gif'),
            story_thumbnail = SimpleUploadedFile('small.gif', testfile, content_type = 'image/gif'),)
        story.save()
        page = self.client.get('/story/{}'.format(story.id))
        self.assertEqual(page.status_code, 200)