from django.test import TestCase
from .views import index

class TestMainViews(TestCase):

    def test_home_page(self):
        page = self.client.get('/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'main/index.html')