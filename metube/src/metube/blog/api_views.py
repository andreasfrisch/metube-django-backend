"""
Request handlers for blog API
"""

import json

from datetime import datetime
from typing import Dict, List
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from metube.utils import json_response, token_required
from metube.blog.models import Post, Paragraph

def _complete_post_as_dict(post: Post) -> Dict:
    post_dict = post.as_dict()
    post_paragraphs: List[Paragraph] = Paragraph.objects.filter(post=post)
    post_dict["paragraphs"] = [p.as_dict() for p in post_paragraphs]
    return post_dict

def specific_post(request, slug):
    """
    Get one blog post as JSON based on slug
    """
    post = get_object_or_404(Post, slug=slug)
    return json_response(_complete_post_as_dict(post))

def specific_post_by_id(request, pid):
    """
    Get one blog post as JSON based on id
    """
    post = get_object_or_404(Post, id=pid)
    return json_response(_complete_post_as_dict(post))

def newest(request):
    """
    Get newest blog post as JSON
    """
    post = Post.objects.all().order_by('-date')[0]
    return json_response(
        {"slug": post.slug},
        status=200
    )

def create_post(request):
    """
    Create new blog post from JSON
    """
    if request.method == "POST":
        post_data = json.loads(request.body)
        post = Post(
            title=post_data['title'],
            author=post_data['author'],
            date=datetime.fromtimestamp(post_data['date_unix_seconds']),
            tags=",".join(post_data['tags'])
        )
        post.save()
        for paragraph in post_data["paragraphs"]:
            Paragraph(
                content=paragraph["content"],
                type=paragraph["type"],
                order=paragraph["order"],
                post=post
            ).save()
        return HttpResponse(status=200)
    return HttpResponse(status=405)

def posts(request):
    """
    Get a list of all blog posts as JSON
    """
    if request.method == "GET":
        return json_response([post.as_dict(with_content=False) for post in Post.objects.all()])
    elif request.method == "POST":
        return create_post(request)
    else:
        return HttpResponse(status=500)
