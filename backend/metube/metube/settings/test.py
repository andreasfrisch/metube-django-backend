from metube.settings.universal import *

ENVIRONMENT = 'testing'
SECRET_KEY = 'u!kw$drrafj^mc-@8!_(pdj-@87)@xp06nd7d&#_ab2$(moe4a'
DEBUG = True
ALLOWED_HOSTS = ["*"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'metube.db',
    }
}
