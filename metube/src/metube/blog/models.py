"""
Blog models
"""

import time
from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone
from enum import Enum


#from metube.blog.post_manipulation import paragraph_string_to_dict

class ParagraphType(Enum):
    TXT = "Text"
    IMG = "Image"
    COD = "Code"


class Post(models.Model):
    """
    A single blog post
    """
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    tags = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title

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
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def as_dict(self):
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
        return post

    def __unicode__(self):
        return self.title


class Paragraph(models.Model):
    """
    A single paragraph for a blog post
    """
    content = models.TextField()
    content_type = models.CharField(
        max_length = 3,
        choices = [(tag.name, tag.value) for tag in ParagraphType]
    )
    order = models.IntegerField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def as_dict(self, with_content=True):
        """
        Convert paragraph object to dictionary
        """
        paragraph = {
            "id": self.id,
            "content": self.content,
            "type": self.content_type,
            "order": self.order
        }
        return paragraph

    def __str__(self):
        return "%s--%d" % (self.post.slug, self.order)
