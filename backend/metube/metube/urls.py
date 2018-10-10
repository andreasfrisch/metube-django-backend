"""
Metube URL Configuration
"""

# from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from metube.views import RootPageView, home

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', RootPageView.as_view(), name='root'),
    path('api/', include([
        path('auth/', include('metube.authentication.api_urls')),
        path('blog/', include('metube.blog.api_urls')),
        path('gallery/', include('metube.gallery.api_urls')),
    ])),
]
