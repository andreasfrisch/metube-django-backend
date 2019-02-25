"""
Metube URL Configuration
"""

from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from metube.views import RootPageView, home

urlpatterns = [
    path('', RootPageView.as_view(), name='root'),
    path('admin/', admin.site.urls),
    path('api/', include([
        path('docs/', TemplateView.as_view(template_name='documentation_portal.html')),
        path('auth/', include('metube.authentication.api_urls')),
        path('blog/', include('metube.blog.api_urls')),
        # path('gallery/', include('metube.gallery.api_urls')),
    ])),
]

