"""
Request handlers for the authentication API
"""

import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib import auth
from django.http import HttpResponse
from metube.authentication.models import Token
from metube.utils import json_response, token_required

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
                print(exception)
            if user is not None:
                if user.is_active:
                    try:
                        token, _ = Token.objects.get_or_create(user=user)
                        return json_response({
                            'token': token.token,
                            'username': user.username
                        })
                    except Exception as exception:
                        print(exception)
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
