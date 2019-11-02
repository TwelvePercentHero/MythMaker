from django.test import TestCase, Client
from .models import Story

class TestStoryViews(TestCase):
    
    def test_storylist(self):
        page = self.client.get('/storylist/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'stories/storylist.html')

    def test_story(self):
        story = Story(title = 'Test Story', synopsis = 'Test synopsis')
        story.cover_image = open('media/profile_headers/profile-header.png')
        story.save()
        page = self.client.get('/story/{}'.format(story.id))
        self.assertEqual(page.status_code, 200)