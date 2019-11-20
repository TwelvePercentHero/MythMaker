from django.test import TestCase, Client, RequestFactory
from django.contrib.auth.models import User
from .models import Audio
from accounts.models import Membership, MythMakerMembership
from audio.views import audio, audiolist

class TestAudioListView(TestCase):

    def test_audiolist(self):
        user = User.objects.create_user(
            username = 'TestUser',
            email = 'test@test.com',
            password = 'testpassword'
        )
        membership = Membership.objects.create(
            membership_type = 'FR',
            id = '1'
        )
        page = self.client.get('/audiolist/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'audio/audiolist.html')

    def test_audio(self):
        user = User.objects.create_user(
            username = 'TestUser',
            email = 'test@test.com',
            password = 'testpassword'
        )
        membership = Membership.objects.create(
            membership_type = 'FR',
            id = '1'
        )
        audio = Audio.objects.create(
            title = 'Test Audio',
            description = 'This is a Test Description for the Test Audio',
            audio_file = 'media/audio/test_audio_file.mp3',
            cover_image = 'media/cover_images/test-header.jpg',
            audio_thumbnail = 'media/thumbnails/test-thumb-1.jpg',
            creator = user
        )
        page = self.client.get('/audio/{}'.format(audio.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'audio/audio.html')

    def test_audio_upload_not_logged_in(self):
        user = User.objects.create_user(
            username = 'TestUser',
            email = 'test@test.com',
            password = 'testpassword'
        )
        membership = Membership.objects.create(
            membership_type = 'FR',
            id = '1'
        )
        page = self.client.get('/uploadaudio/')
        self.assertRedirects(page, '/login/?next=/uploadaudio/')

    def test_audio_upload_upgrade_required(self):
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
        page = self.client.get('/uploadaudio/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'main/premium.html')

    def test_delete_audio(self):
        user = User.objects.create_user(
            username = 'TestUser',
            email = 'test@test.com',
            password = 'testpassword'
        )
        membership = Membership.objects.create(
            membership_type = 'FR',
            id = '1'
        )
        audio = Audio.objects.create(
            title = 'Test Audio',
            description = 'This is a Test Description for the Test Audio',
            audio_file = 'media/audio/test_audio_file.mp3',
            cover_image = 'media/cover_images/test-header.jpg',
            audio_thumbnail = 'media/thumbnails/test-thumb-1.jpg',
            creator = user
        )
        self.client.login(username = 'TestUser', password = 'testpassword')
        page = self.client.get('/audio/{}'.format(audio.id))
        self.assertEqual(page.status_code, 200)
        response = self.client.get('/audiolist/')
        audio.delete()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Audio.objects.count(), 0)