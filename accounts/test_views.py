from django.test import TestCase

class TestUserViews(TestCase):

    def test_userlist(self):
        page = self.client.get('/userlist/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'registration/userlist.html')

    def test_register_view(self):
        page = self.client.get('/register/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed('registration/register.html')

    
