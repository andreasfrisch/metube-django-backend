"""
Blog models
"""

import time
from django.db import models
from django.utils.text import slugify
from django.utils import timezone
from enum import Enum

class ParagraphType(Enum):
    TXT = "Text"
    IMG = "Image"

class Post(models.Model):
    """
    A single blog post
    """
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    tags = models.CharField(max_length=200) # TODO: foreign key
    author = models.CharField(max_length=100)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title

    def generate_unique_slug(self, field):
        """
        return unique slug if origin slug exists.
        eg: `foo-bar` => `foo-bar-1`
        :param `field` is specific field for title.
        inspired by: https://djangosnippets.org/snippets/10643/
        """
        origin_slug = slugify(field)
        unique_slug = origin_slug
        numb = 1
        while Post.objects.filter(slug=unique_slug).exists():
            unique_slug = '%s-%d' % (origin_slug, numb)
            numb += 1
        return unique_slug

    def get_absolute_url(self):
        """
        Generate canonical URL for Post object
        """
        return ('blog_post_detail', (), {"slug": self.slug})

    def save(self, *args, **kwargs):
        """
        Override save; generate slug based on title
        """
        if not self.slug:
            self.slug = self.generate_unique_slug(self.title)
        super(Post, self).save(*args, **kwargs)

    def as_dict(self, with_content=True):
        """
        Convert post object to dictionary
        """
        post = {
            "id": self.id,
            "title": self.title,
            "slug": self.slug,
            "tags": [t.strip() for t in self.tags.split(',')],
            "author": self.author,
            "date_unix_seconds": int(time.mktime(self.date.timetuple())),
        }
        if with_content:
            post["paragraphs"] = [p.as_dict() for p in Paragraph.objects.filter(post=self).order_by('order')]
        return post

    def __unicode__(self):
        return self.title

class Paragraph(models.Model):
    """
    A single paragraph belonging to a blog post
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    order = models.IntegerField()
    type = models.CharField(max_length=3, choices=[(tag, tag.value) for tag in ParagraphType])
    content = models.TextField()
    
    def __str__(self):
        return "%s [%s] %s" % (self.order, self.type, self.content[0:20])
    
    def as_dict(self):
        """
        Convert paragraph into dictionary
        """
        paragraph = {
            "order": self.order,
            "type": self.type,
            "content": self.content,
        }
        return paragraph
