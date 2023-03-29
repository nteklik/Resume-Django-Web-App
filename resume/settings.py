"""
Django settings for resume project.

Generated by 'django-admin startproject' using Django 4.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import django_smtp_ssl
import environ
import os

env = environ.Env(DEBUG=(bool, False))
environ.Env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')

ALLOWED_HOSTS = env('ALLOWED_HOSTS', cast=list)

# Must be defined for Django 4+
CSRF_TRUSTED_ORIGINS = env('CSRF_TRUSTED_ORIGINS', cast=list)

UNDER_MAINTENANCE = False

SITE_DOMAINS = ['berkaymizrak.com', 'berkaymizrak.com.tr']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'user.apps.UserConfig',
    'crispy_forms',
    'storages',
    'import_export',
    'mailqueue',
    'django_celery_beat',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # 'whitenoise.middleware.WhiteNoiseMiddleware',  # White Noise for Heroku

    'resume.CanonicalDomainMiddleware.CanonicalDomainMiddleware',  # Extra
    'redirect_to_non_www.middleware.RedirectToNonWww',  # Extra

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'resume.MaintenanceMiddleware.MaintenanceMiddleware',  # Extra
    # 'resume.ParameterMiddleware.ParameterMiddleware',  # Extra
]

ROOT_URLCONF = 'resume.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',  # Extra
                'user.views.layout',  # Extra
            ],
        },
    },
]

WSGI_APPLICATION = 'resume.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': env.db(),
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

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Istanbul'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

STATICFILES_LOCATION = 'static'
if DEBUG:
    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

    DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
else:
    AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = env('AWS_STORAGE_BUCKET_NAME')

    DEFAULT_FILE_STORAGE = 'resume.custom_storages.MediaStorage'
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

    AWS_S3_REGION_NAME = 'eu-central-1'

    AWS_DEFAULT_ACL = 'public-read'
    AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
    AWS_S3_OBJECT_PARAMETERS = {
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'CacheControl': 'max-age=94608000',
    }

    AWS_LOCATION = 'static'
    STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
    STATIC_ROOT = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)

DEFAULT_PNG = STATIC_URL + 'default.png'
MEDIA_LOCATION = 'media'
IMAGE_SETTINGS_LOCATION = MEDIA_LOCATION + '/image_settings'
DOCUMENT_LOCATION = MEDIA_LOCATION + '/document'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ---------------------------- CRISPY ----------------------------
CRISPY_TEMPLATE_PACK = 'bootstrap4'  # crispy kodu
# ---------------------------- CRISPY ----------------------------


# ---------------------------- GOOGLE RECAPTCHA ----------------------------
GOOGLE_RECAPTCHA_SITE_KEY = env('GOOGLE_RECAPTCHA_SITE_KEY')
GOOGLE_RECAPTCHA_SECRET_KEY = env('GOOGLE_RECAPTCHA_SECRET_KEY')
# ---------------------------- GOOGLE RECAPTCHA ----------------------------


# ---------------------------- EMAIL SETTINGS ----------------------------
# EMAIL_USE_SSL = True
# EMAIL_USE_TLS = False

vars().update(env.email_url())
DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL')
EMAIL_BACKEND = env('EMAIL_BACKEND')
# ---------------------------- EMAIL SETTINGS ----------------------------


# ---------------------------- SSL SERVER SETTINGS ----------------------------
if not DEBUG:
    # Since Cloudflare have automatic redirect to https, this setting causes infinite loop.
    # SECURE_SSL_REDIRECT = env('SECURE_SSL_REDIRECT')
    SESSION_COOKIE_SECURE = env('SESSION_COOKIE_SECURE')
    CSRF_COOKIE_SECURE = env('CSRF_COOKIE_SECURE')
    # PREPEND_WWW = False

    SET_SSL_MODE = env('SET_SSL_MODE', default=False)
    if SET_SSL_MODE:
        SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
        os.environ['HTTPS'] = 'on'
        os.environ['wsgi.url_scheme'] = 'https'
# ---------------------------- SSL SERVER SETTINGS ----------------------------


# ---------------------------- ERROR 403 HANDLER ----------------------------
CSRF_FAILURE_VIEW = 'user.views.csrf_failure'
# ---------------------------- ERROR 403 HANDLER ----------------------------


# ---------------------------- CELERY ----------------------------
CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL', 'redis://redis_resume:6379/0')
CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND', 'redis://redis_resume:6379/0')

CELERY_ACCEPT_CONTENT = ['json']
CELERY_RESULT_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Europe/Istanbul'
CELERY_ENABLE_UTC = False  # DEFAULT True
CELERYBEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'

# CELERY_IMPORTS = ("user.tasks",)

CELERY_TASK_RESULT_EXPIRES = 60 * 60 * 24 * 2  # Seconds (2 days)
BROKER_POOL_LIMIT = 1
BROKER_HEARTBEAT = None
USER_AGENTS_CACHE = None
# ---------------------------- CELERY ----------------------------


# ---------------------------- MAILQUEUE ----------------------------
# pip install django-mail-queue
# The settings for the mail queue package.

# If you're using Celery, set this to True
MAILQUEUE_CELERY = True  # DEFAULT False

# Enable the mail queue. If this is set to False, the mail queue will be disabled and emails will be
# sent immediately instead.
MAILQUEUE_QUEUE_UP = True

# Maximum amount of emails to send during each queue run
MAILQUEUE_LIMIT = 1

# If MAILQUEUE_STORAGE is set to True, will ignore your default storage settings
# and use Django's filesystem storage instead (stores them in MAILQUEUE_ATTACHMENT_DIR)
# MAILQUEUE_STORAGE = True
# MAILQUEUE_ATTACHMENT_DIR = 'mailqueue-attachments'
# ---------------------------- MAILQUEUE ----------------------------
