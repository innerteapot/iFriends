"""
Django settings for iFriends project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'gpmwo%)#uhz^7ltyy@xvn*zj0z46p@k@)^ng8f81sb*!jj5ak*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'People',
    'Comments',
    'Quotes',
    'Custom',
    'Poll',
    'Log',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'iFriends.middleware.custom.CustomRequestLogger',
    'iFriends.middleware.custom.CustomViewLogger',
    'iFriends.middleware.custom.CustomResponseLogger',
    'iFriends.middleware.custom.CustomExceptionLogger',
    'iFriends.middleware.custom.AddFooter',
    'iFriends.middleware.custom.PersonIPAddressCapture',
)

ROOT_URLCONF = 'iFriends.urls'

WSGI_APPLICATION = 'wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'innerteapot$iFriendsDB',
        'USER': 'innerteapot',
        'PASSWORD': 'SbHnH6bQzpyeiCb8BEb6dKu35uS8z7Vf',
        'HOST': 'innerteapot.mysql.pythonanywhere-services.com',
        'PORT': '3306',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ["/home/innerteapot/src/iFriends/templates"],
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

#TEMPLATE_DIRS = (
#    # Put strings here, like "/home/html/django_templates" or
#    # "C:/www/django/templates".
#    # Always use forward slashes, even on Windows.
#    # Don't forget to use absolute paths, not relative paths.
#    "/home/innerteapot/src/iFriends/templates",
#)

LOGIN_URL ='/Login'
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

