#
# Development settings
# These will be overwritten on deployment from S3
# Do not keep actual secrets in here
#

_ENVIRONMENT = 'development'
_SECRET_KEY = 'u!kw$drrafj^mc-@8!_(pdj-@87)@xp06nd7d&#_ab2$(moe4a'
_DEBUG = True
_ALLOWED_HOSTS = ["*"]


_AWS_ACCESS_KEY_ID = 'AKIAJTBGPBZ54JDETV3Q'
_AWS_SECRET_ACCESS_KEY = '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'

_DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'metube',
        'USER': 'mysql',
        'PASSWORD': 'mysql',
        'HOST': 'database',
        'PORT': '3306',
    }
}
