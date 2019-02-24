"""
Registering Gallery models with admin interface
"""

from django.contrib import admin

from metube.gallery.models import Image
admin.site.register(Image)
