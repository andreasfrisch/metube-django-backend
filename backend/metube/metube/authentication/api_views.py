"""
Request handlers for the authentication API
"""

import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib import auth
from django.http import HttpResponse
from metube.authentication.models import Token
from metube.utils import json_response, token_required

@csrf_exempt
def login(request):
    """
    Login user and return valid access token
    """
    if request.method == 'POST':
        parsed_body = json.loads(request.body)
        username = parsed_body["username"]
        password = parsed_body["password"]

        if username is not None and password is not None:
            try:
                user = auth.authenticate(username=username, password=password)
            except Exception as exception:
                print(exception) #TODO 01: logging
            if user is not None:
                if user.is_active:
                    try:
                        token, _ = Token.objects.get_or_create(user=user)
                        return json_response({
                            'token': token.token,
                            'username': user.username
                        })
                    except Exception as exception:
                        print(exception) # TODO 01: logging
                else:
                    return json_response({
                        'error': 'Invalid User'
                    }, status=400)
            else:
                return json_response({
                    'error': 'Invalid Username/Password'
                }, status=400)
        else:
            return json_response({
                'error': 'Invalid Data'
            }, status=400)
    elif request.method == 'OPTIONS':
        return json_response({})
    else:
        return json_response({
            'error': 'Invalid Method'
        }, status=405)

@token_required
def logout(request):
    """
    Logout by invalidating user access token
    """
    if request.method == 'POST':
        request.token.delete()
        return json_response({
            'status': 'success'
        })
    elif request.method == 'OPTIONS':
        return json_response({})
    else:
        return json_response({
            'error': 'Invalid Method'
        }, status=405)

@token_required
def verify(request):
    """
    Verify correctness of access token
    """
    return HttpResponse(status=200)


#
# ## TODO 02: MOVE LOGIN
#
# from django.contrib.auth import authenticate
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.authtoken.models import Token
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import AllowAny
# from rest_framework.status import (
#     HTTP_400_BAD_REQUEST,
#     HTTP_404_NOT_FOUND,
#     HTTP_200_OK
# )
# from rest_framework.response import Response
#
#
# @csrf_exempt
# @api_view(["POST"])
# @permission_classes((AllowAny,))
# def login(request):
#     username = request.data.get("username")
#     password = request.data.get("password")
#     if username is None or password is None:
#         return Response({'error': 'Please provide both username and password'},
#                         status=HTTP_400_BAD_REQUEST)
#     user = authenticate(username=username, password=password)
#     if not user:
#         return Response({'error': 'Invalid Credentials'},
#                         status=HTTP_404_NOT_FOUND)
#     token, _ = Token.objects.get_or_create(user=user)
#     return Response({'token': token.key},
#                     status=HTTP_200_OK)