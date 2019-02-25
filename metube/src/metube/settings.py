"""
Django settings for metube project.
"""

import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
VERSION = 0.2
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 
# Environmental Settings
# 

SECRET_KEY = os.environ["METUBE_SECRET_KEY"]
ENVIRONMENT = os.environ["METUBE_ENVIRONMENT"]

DEBUG = False if not "METUBE_DEBUG" in os.environ else os.environ["METUBE_DEBUG"] == "TRUE"
ALLOWED_HOSTS = os.environ.get("METUBE_ALLOWED_HOSTS", "localhost").split(",")

DEFAULT_DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'metube.db'
    }
}
DATABASES = (
  json.loads(os.environ["METUBE_DATABASES"])
  if "APP_DATABASES" in os.environ
  else DEFAULT_DATABASES
)

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# 
# Base Settings
# Environment agnostic
# 

# Application definition
WSGI_APPLICATION = 'metube.wsgi.application'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'storages',
    'metube.authentication',
    'metube.gallery',
    'metube.blog'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'metube.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'docs')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Prettify unit tests
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
NOSE_ARGS = ['--with-spec', '--spec-color']
