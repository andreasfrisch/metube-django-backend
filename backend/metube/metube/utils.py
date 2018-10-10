"""
    Utility functions used throughout the backend
    Author: Andreas Frisch
"""

import json
from django.http import HttpResponse
from metube.authentication.models import Token

def json_response(response_dict, status=200):
    """
    Convert dictionary to JSON and return as a HTTP Response with JSON content
    """
    response = HttpResponse(
        json.dumps(response_dict),
        content_type="application/json",
        status=status
    )
    response['Access-Control-Allow-Origin'] = '*'
    response['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
    return response

def token_required(func):
    """
    Decorator to assert valid accesstoken in request
    """
    def inner(request, *args, **kwargs):
        try:
            if request.method == 'OPTIONS':
                return func(request, *args, **kwargs)
            auth_header = request.META.get('HTTP_AUTHORIZATION', None)
            if auth_header is not None:
                tokens = auth_header.split(' ')
                if len(tokens) == 2 and tokens[0] == 'Token':
                    token = tokens[1]
                    try:
                        request.token = Token.objects.get(token=token)
                        return func(request, *args, **kwargs)
                    except Token.DoesNotExist:
                        return json_response({
                            'error': 'Token not found'
                        }, status=401)
            return json_response({
                'error': 'Invalid Header'
            }, status=401)
        except Exception as exception:
            print(exception) # TODO 01: using logging framework instead

    return inner