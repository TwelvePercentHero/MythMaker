from django.test import TestCase

class TestStoryViews(TestCase):

    def test_storylist(self):
        page = self.client.get('/storylist/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'stories/storylist.html')