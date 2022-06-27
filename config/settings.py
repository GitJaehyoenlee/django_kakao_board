"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 4.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import json
import os
from pathlib import Path

DEV_MODE = True

# [Leny] Auth model Change
AUTH_USER_MODEL = 'ks_accounts.User'

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# [Leny] Auth model Change <start>
SECRET_FILE = os.path.join(BASE_DIR, 'secret.json')

with open(SECRET_FILE) as f:
    SECRETS = json.loads(f.read())
# [Leny] Auth model Change <end>

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = SECRETS['SECRET_KEY']


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# [Leny] Auth model Change <end>
if DEV_MODE == True:
    ALLOWED_HOSTS = ['127.0.0.1']
else:
    ALLOWED_HOSTS = ['*',]

# Application definition

INSTALLED_APPS = [
    # Default System APPS
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 3rd Party APPS

    # User Definition APPS
    'ks_accounts',
    'blog_board',
    'blog_reply',
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

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

if DEV_MODE == True:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': SECRETS['DB_NAME'],
            'USER': SECRETS['DB_USER'],
            'PASSWORD': SECRETS['DB_PASSWORD'],
            'HOST': SECRETS['DB_HOST'],
            'PORT': SECRETS['DB_PORT'],
            'OPTIONS:': {
                'init_command': 'SET sql_mode="STRICT_TRANS_TABLES"'
            }
        }
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
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

if DEV_MODE == True:
    STATIC_URL = 'static/'
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

else:
    # [Leny] AWS Setting <start>
    AWS_ACCESS_KEY_ID = SECRETS["AWS_ACCESS_KEY_ID"]
    AWS_SECRET_ACCESS_KEY = SECRETS["AWS_SECRET_ACCESS_KEY"]
    AWS_REGION = 'ap-northeast-2'
    AWS_STORAGE_BUCKET_NAME = SECRETS["AWS_STORAGE_BUCKET_NAME"]
    AWS_S3_CUSTOM_DOMAIN = '%s.s3.%s.amazonaws.com' % (AWS_STORAGE_BUCKET_NAME, AWS_REGION)
    AWS_S3_OBJECT_PARAMETERS = {
        'CacheControl': 'max-age=86400',
    }

    # [Leny] AWS 세팅 중, S3 스토리지에 정상적으로 연결되지 않는 경우, None으로 1차 실행 후, -> static 진행
    # python manage.py collectstatic
    AWS_DEFAULT_ACL = 'public-read'
    # AWS_DEFAULT_ACL = 'None'
    AWS_LOCATION = 'static'
    AWS_MEDIA_LOCATION = 'media'

    STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

    MEDIA_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_MEDIA_LOCATION)
    # MEDIA_ROOT = 'storages.backends.s3boto3.S3Boto3Storage'
    DEFAULT_FILE_STORAGE = 'config.asset_storage.MediaStorage'

    # [Leny] AWS Setting <END>

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# [Leny] GOOGLE SMTP SETTING
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.googlemail.com'
EMAIL_HOST_USER = SECRETS["EMAIL_HOST_USER"]
EMAIL_HOST_PASSWORD =SECRETS["EMAIL_HOST_PASSWORD"]
EMAIL_USE_TLS = True
EMAIL_PORT = 587
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 1

# [Leny] Kakao Rest API KEY
KAKAO_REST_API_KEY = SECRETS["KAKAO_REST_API_KEY"]
