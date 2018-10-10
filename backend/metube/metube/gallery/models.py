"""
Gallery models
"""

import time
from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone

from django.db import models

class Image(models.Model):
    """
    A single image
    """
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    tags = models.CharField(max_length=200)
    date = models.DateField(default=timezone.now)
    image = models.ImageField(upload_to="images")
    
    def __str__(self):
        if self.title:
            return self.title
        else:
            return "unnamed image (%d)" % self.id

    def __unicode__(self):
        if self.title:
            return self.title
        else:
            return "unnamed image (%d)" % self.id

    def save(self, *args, **kwargs):
        """
        Override save; generate slug based on title
        """
        if self.title:
            if not self.slug:
                self.slug = slugify(self.title)
        super(Image, self).save(*args, **kwargs)