import os
from pathlib import Path

import dj_database_url
import environ
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Initialize the environment variable
# See https://django-environ.readthedocs.io/en/latest/
env = environ.Env()

# Read environment variables from .env
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# SECURITY WARNING: keep the secret key used in production secret!
# Check Makefile for command to generate SECRET_KEY
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-override-from-env-file')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(int(os.environ.get('DEBUG', 1)))

ALLOWED_HOSTS = [host for host in os.environ.get('ALLOWED_HOSTS', '*').split(',')]

# CORS configuration
CORS_ORIGIN_ALLOW_ALL = bool(int(os.environ.get('CORS_ORIGIN_ALLOW_ALL', 0)))
if os.environ.get('CORS_ALLOWED_ORIGINS', None):
    CORS_ALLOWED_ORIGINS = [host for host in os.environ.get('CORS_ALLOWED_ORIGINS').split(',')]

# CSRF configurations
if os.environ.get('CSRF_TRUSTED_ORIGINS', None):
    CSRF_TRUSTED_ORIGINS = [host for host in os.environ.get('CSRF_TRUSTED_ORIGINS').split(',')]


# App branding
APP_NAME = os.environ.get('APP_NAME', 'MSEDCL Power Purchase Invoice System')
APP_LOGO = os.environ.get(
    'APP_LOGO',
    'https://www.linkpicture.com/q/sample_logo.png'
)

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'corsheaders',
    'drf_yasg',
    'rest_framework',
    'django_filters',
]

# Business Applications (Specific to the project)
BUSINESS_APPS = [
    'core',
    'users',
    'authentication',
    'emailer',
]
INSTALLED_APPS += BUSINESS_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
if os.environ.get('DB_HOST'):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ.get('DB_NAME'),
            'USER': os.environ.get('DB_USER'),
            'PASSWORD': os.environ.get('DB_PASSWORD'),
            'HOST': os.environ.get('DB_HOST'),
            'PORT': os.environ.get('DB_PORT'),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

# Another way to connect to the database. This overides the
# above seetings if DATA_BASE_URL is set in the environment
if os.environ.get('DATABASE_URL'):
    DATABASE_URL = os.environ.get('DATABASE_URL')
    DATABASES['default'] = dj_database_url.parse(DATABASE_URL)

# Email configuration
EMAIL_BACKEND = os.environ.get(
    'EMAIL_BACKEND',
    'django.core.mail.backends.console.EmailBackend',
)
DEFAULT_EMAIL_SENDER = os.environ.get(
    'DEFAULT_EMAIL_SENDER',
    'hello@example.com'
)
EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS', False)
EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_PORT = os.environ.get('EMAIL_PORT', 587)


# REST framework configuration
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'authentication.backends.JWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
     'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
    ],
    'EXCEPTION_HANDLER': 'core.exceptions.core_exception_handler',
    'NON_FIELD_ERRORS_KEY': 'error',
    'DEFAULT_PAGINATION_CLASS': 'core.pagination.CustomPagination',
    'PAGE_SIZE': 10,
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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

AUTH_USER_MODEL = 'users.User'

# JWT token expiration
TOKEN_EXPIRY_DAYS = 1

# SWAGGER settings
SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'api_key': {
            'type': 'apiKey',
            'in': 'header',
            'name': 'Authorization'
        }
    },
}

# Media settings for 'django-storages'
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')

# AWS Location is path prefix for all uploads.
# Preferred to be kept same as Environment
AWS_LOCATION = os.environ.get('ENVIRONMENT')
AWS_QUERYSTRING_AUTH = True
AWS_S3_FILE_OVERWRITE = False

# Files uploaded by Users
MEDIA_ROOT_DEFAULT = os.path.join(BASE_DIR, 'media')
MEDIA_ROOT = os.environ.get('MEDIA_ROOT', MEDIA_ROOT_DEFAULT)
MEDIA_URL = os.environ.get('MEDIA_URL', '/media/')
DEFAULT_FILE_STORAGE = os.environ.get(
    'FILE_STORAGE',
    'django.core.files.storage.FileSystemStorage'
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_STORAGE = os.environ.get(
    'STATICFILES_STORAGE',
    'django.contrib.staticfiles.storage.StaticFilesStorage',
)

# Sentry configuration
sentry_sdk.init(
    dsn=os.environ.get('SENTRY_DSN', None),
    integrations=[DjangoIntegration()],
    traces_sample_rate=1.0,
    send_default_pii=True,
    environment=os.environ.get('ENVIRONMENT'),
)

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# API configuration
API_PREFIX = 'api/v1/'
