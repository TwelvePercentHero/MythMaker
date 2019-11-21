from django.test import TestCase
from .models import Like, Comment
from django.contrib.auth.models import User

class TestCommunityModels(TestCase):

    def test_story_type_is_a_string(self):
        like = Like(story_type = 'STORY')
        self.assertEqual(like.story_type, str(like))

    def test_like_verbose_name_plural(self):
        self.assertEqual(str(Like._meta.verbose_name_plural), 'Likes')

    def test_comment_verbose_name_plural(self):
        self.assertEqual(str(Comment._meta.verbose_name_plural), 'Comments')



