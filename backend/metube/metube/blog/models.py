"""
Blog models
"""

import time
from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone

from metube.blog.post_manipulation import paragraph_string_to_dict

class Post(models.Model):
    """
    A single blog post
    """
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    tags = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    date = models.DateField(default=timezone.now)
    content = models.TextField()

    def __str__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        #TODO: what does this do
        """
        <Fill this out>
        """
        return ('blog_post_detail', (), {"slug": self.slug})

    def save(self, *args, **kwargs):
        """
        Override save; generate slug based on title
        """
        if not self.slug:
            self.slug = slugify(self.title)
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
            post["paragraphs"] = [paragraph_string_to_dict(p) for p in self.content.split('\n\n')]
        return post

    def __unicode__(self):
        return self.title
