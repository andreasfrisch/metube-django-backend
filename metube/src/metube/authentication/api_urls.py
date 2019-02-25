"""
URL handlers for authentication API
"""

from django.urls import path
from django.views.generic import TemplateView
from metube.authentication.api_views import login, logout, verify

urlpatterns = [
    path('docs/', TemplateView.as_view(template_name='auth_api.html')),
    path('login/', login),
    path('logout/', logout),
    path('verify/', verify),
]
