"""
Django settings for new_class project.

Generated by 'django-admin startproject' using Django 3.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.


BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-t)ft!#(qolqcp1+gpz*(kvf+_udiyi=@&p4^uy-0%86yew$dom'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['https://vishal-newclass.herokuapp.com/']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts.apps.AccountsConfig',
    'django_filters',
    'storages',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'new_class.urls'

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

WSGI_APPLICATION = 'new_class.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'database1',
        'USER': 'postgres',
        'PASSWORD':'myAWSpassword',
        'HOST': 'database-2.cynhwernuxwx.ap-south-1.rds.amazonaws.com',
        'PORT':'5432',
    }
}
'''

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR,'db.sqlite3'),

    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS=[
    os.path.join(BASE_DIR,'static')
]
STATIC_ROOT=os.path.join(BASE_DIR,'staticfiles')

MEDIA_URL='/images/'

MEDIA_ROOT=os.path.join(BASE_DIR,'static/images')

#SMTP Configuration

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'vishal.das0911@gmail.com'
EMAIL_HOST_PASSWORD = 'Iloveyou@123'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



#S3 BUCKETS CONFIG

AWS_ACCESS_KEY_ID = 'AKIA3SNIRMVEONQPEB7T'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'vishald.crm.bucket'
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None
AWS_S3_REGION_NAME = 'ap-south-1'
AWS_S3_USE_SSL = True
#AWS_S3_ADDRESSING_STYLE = 'path'

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3StaticStorage'

#AWS_S3_PROXIES = ‘http’:‘foo.bar:3128’,‘http://hostname’: ‘foo.bar:4012’
#AWS_S3_ENDPOINT_URL = 'http://vishald.crm.bucket.s3-website.ap-south-1.amazonaws.com'
#AWS_S3_CUSTOM_DOMAIN = 'cdn.mydomain.com'
#AWS_QUERYSTRING_AUTH = True
#GZIP_CONTENT_TYPES = ''
#AWS_IS_GZIPPED = True
#AWS_S3_OBJECT_PARAMETERS = '{}'

