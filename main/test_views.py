from django.test import TestCase
from .views import index, about, privacy

class TestMainViews(TestCase):

    def test_home_page(self):
        page = self.client.get('/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'main/index.html')

    def test_about_page(self):
        page = self.client.get('/about/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'main/about.html')

    def test_privacy_page(self):
        page = self.client.get('/privacy/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'main/privacy.html')