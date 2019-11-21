from django.test import TestCase
from .forms import CommentUpload

class TestCommentForm(TestCase):

    def test_comment_without_text(self):
        form = CommentUpload({
            'comment' : ''
        })
        self.assertFalse(form.is_valid())

    def test_comment_with_text(self):
        form = CommentUpload({
            'comment' : 'This is a Test Comment'
        })
        self.assertTrue(form.is_valid())