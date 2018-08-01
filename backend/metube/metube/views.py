import textwrap

from django.http import HttpResponse
from django.views.generic.base import View

from metube.secret_settings import _ENVIRONMENT


class RootPageView(View):

    def dispatch(request, *args, **kwargs):
        response_text = textwrap.dedent('''\
            <html>
            <head>
                <title>Greetings to the world</title>
            </head>
            <body>
                <h1>Greetings to the world</h1>
                <p>Environment: %s</p>
            </body>
            </html>
        ''' % _ENVIRONMENT)
        return HttpResponse(response_text)