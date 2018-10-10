"""
Authentication framework models
"""

import binascii
import os
from django.contrib.auth.models import User
from django.db import models

def generate_access_token():
    """
    Generate access token
    """
    #TODO 02: use proper JWT library
    return binascii.hexlify(os.urandom(20)).decode()

class Token(models.Model):
    """
    Linking users and access tokens
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=40, primary_key=True)
    created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        """
        Override save function; ensure an access token is stored
        """
        if not self.token:
            self.token = generate_access_token()
        return super(Token, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.token
