"""
Test suite for blog app
"""
from django.test import TestCase
from metube.blog.models import Post, Paragraph, ParagraphType

class ArchiveTestCase(TestCase):
    def setUp(self):
        post1 = Post.objects.create(
            title="Test 1",
            tags="test",
            author="Testing Man"
        )
        Paragraph.objects.create(
            post = post1,
            type = ParagraphType.TXT,
            content = "Some paragraph content",
            order = 0
        )
        Paragraph.objects.create(
            post = post1,
            type = ParagraphType.TXT,
            content = "Some other paragraph content",
            order = 1
        )
        
        post2 = Post.objects.create(
            title="Test 2",
            tags="test, demo",
            author="Testing Man"
        )
        Paragraph.objects.create(
            post = post2,
            type = ParagraphType.TXT,
            content = "Content is Content\n\r   Is Content",
            order = 0
        )
        
    
    def test_archive_length(self):
        archive = Post.objects.all()
        self.assertEqual(len(archive), 2)
    
    def test_all_paragraphs_length(self):
        paragraphs = Paragraph.objects.all()
        self.assertEqual(len(paragraphs), 3)
