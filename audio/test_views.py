from django.test import TestCase, Client, RequestFactory
from django.contrib.auth.models import User
from .models import Audio
from accounts.models import Membership
from audio.views import audio, audiolist

class TestAudioListView(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username = 'TestUser',
            email = 'test@test.com',
            password = 'testpassword'
        )
        test_membership = Membership.objects.create(
            membership_type = 'FR'
        )
        audio = Audio.objects.create(
            title = 'Test Audio',
            description = 'This is a Test Description for the Test Audio',
            audio_file = 'media/audio/test_audio_file.mp3',
            cover_image = 'media/cover_images/test-header.jpg',
            audio_thumbnail = 'media/thumbnails/test-thumb-1.jpg',
            creator = self.user
        )

    '''def test_audiolist(self):
        request = self.factory.get('/audiolist/')
        request.user = self.user
        response = audiolist(request)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'audio/audiolist.html)'''

    def test_audio(self):
        audio = Audio.objects.get(title = 'Test Audio')
        response = self.client.get('/audio/{}'.format(audio.id))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'audio/audio.html')