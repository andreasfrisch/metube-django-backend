"""
URL handlers for blog API
"""

from django.urls import path
from metube.blog.api_views import newest, posts, specific_post, specific_post_by_id

urlpatterns = [
    path('posts/', posts, name='blog_posts'),
    path('posts/newest', newest, name='newest'),
    path('posts/id/<int:pid>', specific_post_by_id),
    path('posts/<slug:slug>', specific_post),
]
