import textwrap

from django.http import HttpResponse
from django.views.generic.base import View


class RootPageView(View):

    def dispatch(request, *args, **kwargs):
        response_text = textwrap.dedent('''\
            <html>
            <head>
                <title>Greetings to the world</title>
            </head>
            <body>
                <h1>Greetings to the world</h1>
                <p>Hello, world!</p>
                <p>This is a test 8</p>
            </body>
            </html>
        ''')
        return HttpResponse(response_text)