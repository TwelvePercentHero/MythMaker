from django.test import TestCase
from .models import Story

'''class TestStoryViews(TestCase):
    
    def test_storylist(self):
        page = self.client.get('/storylist/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'stories/storylist.html')

    def test_story(self):
        story = Story(
            title = 'Test Story',
            synopsis = 'Test synopsis',
            story = 'This is a Test Story',
            cover_image = 'media/cover_images/test-header.jpg',
            story_thumbnail = 'media/thumbnails/test-thumb-1.jpg'
        )
        story.save()
        page = self.client.get('/story/{}'.format(story.id))
        self.assertEqual(page.status_code, 200)'''