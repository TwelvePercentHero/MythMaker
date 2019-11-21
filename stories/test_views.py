from django.test import TestCase
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

    def test_story_upload_not_logged_in(self):
        user = User.objects.create_user(
            username = 'TestUser',
            email = 'test@test.com',
            password = 'testpassword'
        )
        membership = Membership.objects.create(
            membership_type = 'FR',
            id = '1'
        )
        page = self.client.get('/uploadstory/')
        self.assertRedirects(page, '/login/?next=/uploadstory/')

    def test_story_upload_logged_in(self):
        user = User.objects.create_user(
            username = 'TestUser',
            email = 'test@test.com',
            password = 'testpassword'
        )
        membership = Membership.objects.create(
            membership_type = 'FR',
            id = '1'
        )
        self.client.login(username = 'TestUser', password = 'testpassword')
        page = self.client.get('/uploadstory/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'stories/uploadstory.html')

    def test_delete_story(self):
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
        self.client.login(username = 'TestUser', password = 'testpassword')
        page = self.client.get('/story/{}'.format(story.id))
        self.assertEqual(page.status_code, 200)
        response = self.client.get('/storylist/')
        story.delete()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Story.objects.count(), 0)