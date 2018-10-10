"""
Request handlers for gallery API
"""

import json

from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.core.files.base import ContentFile
from datetime import datetime
from metube.utils import json_response
from metube.gallery.models import Image
from metube.utils import token_required
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt #TODO: is this required?
@token_required
def create_image(request):
    """
    Create new image from request
    """
    if request.method == "POST":
        try:
            new_image = Image(
                image = request.FILES['file'],
                title = request.POST.get('title'),
                tags = request.POST.get('tags'),
            ).save()
        except Exception as e:
            print("Error saving new image: %s" % e) # TODO 01: Logging
            return HttpResponse(status=500)
        return HttpResponse(status=200)
    return HttpResponse(status=405)

@csrf_exempt #TODO: is this required?
def images(request):
    """
    Get a list of all gallery images as json
    """
    if request.method == "GET":
        return json_response([imageObject.image.url for imageObject in Image.objects.all()])
    
    elif request.method == "POST":
        return create_image(request)
        