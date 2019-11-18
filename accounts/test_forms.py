from django.test import TestCase
from .forms import MythMakerForm, UpdateProfile
from django.contrib.auth.models import User
from django.test import Client
from .models import MythMaker, Membership

class TestMythMakerForm(TestCase):
    def test_mythmaker_registration_form_is_valid(self):
        form = MythMakerForm(
            {
            'username' : 'TestUser',
            'email' : 'mythmakerinchief@gmail.com',
            'password1' : 'testpassword',
            'password2' : 'testpassword'
            }
        )
        self.assertTrue(form.is_valid())

    def test_invalid_password_entry(self):
        form = MythMakerForm(
            {
                'username' : 'TestUser',
                'email' : 'mythmakerinchief@gmail.com',
                'password1' : 'testpassword',
                'password2' : 'testpassword2'
            }
        )
        self.assertEqual(
            form.errors['password2'], [u"The two password fields didn't match."]
        )

class TestUpdateProfileForm(TestCase):
    def setUp(self):
        test_user = User.objects.create(
            username = 'TestUser',
            email = 'mythmakerinchief@gmail.com',
            password = 'testpassword'
        )
        test_membership = Membership.objects.create(
            membership_type = 'FR'
        )
        c = Client()
        c.login(username = 'TestUser', password = 'testpassword')
        
    def test_update_tagline(self):
        user = User.objects.get(username = 'TestUser')
        mythmaker = MythMaker.objects.get(user = user)
        form = UpdateProfile({'tagline' : 'This is a test tagline'})
        form.save()
        self.assertTrue(form.is_valid())