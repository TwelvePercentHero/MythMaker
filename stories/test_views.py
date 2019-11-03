from django.test import TestCase, Client
from .models import Story

from accounts.forms import MythMakerForm, ExtendedAuthForm

class TestStoryViews(TestCase):

    c = Client()

    def setUp(self):
        user = MythMakerForm({'username': 'Test',
                                    'email': 'mythmakerinchief@gmail.com',
                                    'password1': 'testing123',
                                    'password2': 'testing123'})
        user.is_active = True
        test_user = user.save()
        authenticate_test = ExtendedAuthForm({'username': 'Test',
                                                'password': 'testing123'})
        authenticate_test.save()

        logged_in = self.c.login(username = 'Test', password = 'testing123')
    
    '''def test_storylist(self):
        page = self.c.get('/storylist/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'stories/storylist.html')

    def test_story(self):
        story = Story(title = 'Test Story', synopsis = 'Test synopsis')
        story.cover_image = open('media/profile_headers/profile-header.png')
        story.save()
        page = self.c.get('/story/{}'.format(story.id))
        self.assertEqual(page.status_code, 200)'''