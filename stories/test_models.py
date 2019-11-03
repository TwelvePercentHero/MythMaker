from django.test import TestCase
from .models import Story

class TestStoryModel(TestCase):

    def test_title_is_a_string(self):
        story = Story(title = 'Test Story Title')
        self.assertEqual(story.title, str(story))

    def test_verbose_name_plural(self):
        self.assertEqual(str(Story._meta.verbose_name_plural), 'Stories')