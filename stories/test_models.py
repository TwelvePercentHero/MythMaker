from django.test import TestCase, Client
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Story

testfile = (
    b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x00\x00\x00\x21\xf9\x04'
    b'\x01\x0a\x00\x01\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02'
    b'\x02\x4c\x01\x00\x3b'
    )

class TestStoryModel(TestCase):

    def test_title_is_a_string(self):
        story = Story(title = 'Test Story Title')
        self.assertEqual(story.title, str(story))

    def test_verbose_name_plural(self):
        self.assertEqual(str(Story._meta.verbose_name_plural), 'Stories')