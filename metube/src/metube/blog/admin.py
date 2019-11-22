"""
Registering Blog items with admin interface
"""

from django.contrib import admin

from metube.blog.models import Post, Paragraph
admin.site.register(Post)
admin.site.register(Paragraph)
