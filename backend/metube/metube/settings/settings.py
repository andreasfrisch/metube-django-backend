#
# Development settings
# These will be overwritten on deployment from S3
# Do not keep actual secrets in here
#

from metube.settings.universal import *

ENVIRONMENT = 'development'
SECRET_KEY = 'u!kw$drrafj^mc-@8!_(pdj-@87)@xp06nd7d&#_ab2$(moe4a'
DEBUG = True
ALLOWED_HOSTS = ["*"]

AWS_ACCESS_KEY_ID = 'something'
AWS_SECRET_ACCESS_KEY = 'orother'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'metube',
        'USER': 'mysql',
        'PASSWORD': 'mysql',
        'HOST': 'database',
        'PORT': '3306',
    }
}
