from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from .models import Story
from accounts.models import Membership
from .views import story, storylist

class TestStoryViews(TestCase):
    
    def test_storylist(self):
        user = User.objects.create_user(
            username = 'TestUser',
            email = 'test@test.com',
            password = 'testpassword'
        )
        membership = Membership.objects.create(
            membership_type = 'FR',
            id = '1'
        )
        page = self.client.get('/storylist/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'stories/storylist.html')

    def test_story(self):
        user = User.objects.create_user(
            username = 'TestUser',
            email = 'test@test.com',
            password = 'testpassword'
        )
        membership = Membership.objects.create(
            membership_type = 'FR',
            id = '1'
        )
        story = Story.objects.create(
            title = 'Test Story',
            author = user,
            synopsis = 'This is a Test Synopsis for the Test Story',
            story = 'This is a Test Story for the Test Story',
            cover_image = 'media/cover_images/test-header.jpg',
            story_thumbnail = 'media/thumbnails/test-thumb-1.jpg'
        )
        page = self.client.get('/story/{}'.format(story.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'stories/story.html')