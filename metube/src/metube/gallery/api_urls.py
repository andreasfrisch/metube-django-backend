"""
URL handlers for gallery API
"""

from django.urls import path
from metube.gallery.api_views import images

urlpatterns = [
    path('images/', images, name='gallery_images'),
    #url(r'^images/(?P<slug>[\w-]+)', 'specific_image'),
]
