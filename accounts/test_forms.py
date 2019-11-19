from django.test import TestCase, Client, RequestFactory
from .forms import MythMakerForm, UpdateProfile
from django.contrib.auth.models import User
from .models import MythMaker, Membership

class TestMythMakerForm(TestCase):
    def test_registration_form_is_valid(self):
        form = MythMakerForm(
            {
            'username' : 'TestUser',
            'email' : 'mythmakerinchief@gmail.com',
            'password1' : 'testpassword',
            'password2' : 'testpassword'
            }
        )
        self.assertTrue(form.is_valid())

    def test_registration_form_empty(self):
        form = MythMakerForm(
            {
                'username' : '',
                'email' : '',
                'password1' : '',
                'password2' : ''
            }
        )
        self.assertFalse(form.is_valid())

    def test_registration_without_username(self):
        form = MythMakerForm(
            {
                'username' : '',
                'email' : 'test@test.com',
                'password1' : 'password1',
                'password2' : 'password1'
            }
        )
        self.assertFalse(form.is_valid())

    def test_registration_without_email(self):
        form = MythMakerForm(
            {
                'username' : 'TestUser',
                'email' : '',
                'password1' : 'password1',
                'password2' : 'password1'
            }
        )
        self.assertFalse(form.is_valid())

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

'''class TestUpdateProfileForm(TestCase):
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
        
    def test_update_tagline(self):
        c = Client()
        c.login(username = 'TestUser', password = 'testpassword')
        form = UpdateProfile({'tagline' : 'This is a test tagline'})
        form.save()
        self.assertTrue(form.is_valid())'''