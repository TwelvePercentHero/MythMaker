from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from .models import Story
from accounts.models import Membership
from .views import story, storylist

class TestStoryViews(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username = 'TestUser',
            email = 'test@test.com',
            password = 'testpassword'
        )
        membership = Membership.objects.create(
            membership_type = 'FR'
        )
        story = Story.objects.create(
            title = 'Test Story',
            author = self.user,
            synopsis = 'This is a Test Synopsis for the Test Story',
            story = 'This is a Test Story for the Test Story',
            cover_image = 'media/cover_images/test-header.jpg',
            story_thumbnail = 'media/thumbnails/test-thumb-1.jpg'
        )
    
    def test_storylist(self):
        request = self.factory.get('/storylist/')
        request.user = self.user
        response = storylist(request)

        self.assertEqual(response.status_code, 200)

    def test_story(self):
        story = Story.objects.get(title = 'Test Story')
        response = self.client.get('/story/{}'.format(story.id))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'stories/story.html')