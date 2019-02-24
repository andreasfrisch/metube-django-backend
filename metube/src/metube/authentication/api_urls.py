"""
URL handlers for authentication API
"""

from django.urls import path
from metube.authentication.api_views import login, logout, verify

urlpatterns = [
    path('login/', login),
    path('logout/', logout),
    path('verify/', verify),
]
