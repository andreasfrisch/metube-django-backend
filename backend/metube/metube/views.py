import textwrap

from django.http import HttpResponse
from django.views.generic.base import View
from django.shortcuts import render

from metube.settings.settings import VERSION, ENVIRONMENT


class RootPageView(View):

    def dispatch(request, *args, **kwargs):
        response_text = textwrap.dedent('''\
            <html>
            <head>
                <title>Greetings to the world</title>
            </head>
            <body>
                <h1>Greetings to the world</h1>
                <h2>Version: %s</h2>
                <p>Environment: %s</p>
            </body>
            </html>
        ''' % (ENVIRONMENT, VERSION))
        return HttpResponse(response_text)

def home(request):
    """
    Handle request for main page
    """
    template = "index.html"
    return render(request, template)
