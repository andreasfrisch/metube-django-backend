"""
Test suite for blog app
"""
from django.test import TestCase
from backend.blog.models import Post

class ArchiveTestCase(TestCase):
    def setUp(self):
        Post.objects.create(
            title="Test 1",
            tags="test",
            author="Testing Man",
            content="This is a test"
        )
    
    def test_archive_length(self):
        archive = Post.objects.all()
        self.assertEqual(len(archive), 1)
    