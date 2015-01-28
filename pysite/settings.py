"""
Django settings for pysite project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '%8$*&5n)1#o=2(++3fn+v(xmnf78ua71k0!#&v5!j5cm6au(gp'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',

	#A
	# 'site_user',	
	
	'siteuser',
	'attendance',
	'behaviour',
	'points',

	# 'tastypie',
	# 'tastypie_mongoengine',

	#A-
)

MIDDLEWARE_CLASSES = (
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',

	# A
	'django.contrib.sessions.middleware.SessionMiddleware',

	# A-
)

ROOT_URLCONF = 'pysite.urls'

WSGI_APPLICATION = 'pysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
	'default': {
		# 'ENGINE': 'django.db.backends.sqlite3',
		'ENGINE': 'django.db.backends.dummy',
		# 'ENGINE': 'django_mongodb_engine',
		# 'User': 'ash',
		# 'Pass': 'a',
		# 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
		'NAME': 'venv1_7cl',
	}
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

# Added

# _MONGODB_USER = 'mongouser'
# _MONGODB_PASSWD = 'password'
# _MONGODB_HOST = 'thehost'
# _MONGODB_NAME = 'thedb'
# _MONGODB_DATABASE_HOST = \
#     'mongodb://%s:%s@%s/%s' \
#     % (_MONGODB_USER, _MONGODB_PASSWD, _MONGODB_HOST, _MONGODB_NAME)

# mongoengine.connect(_MONGODB_NAME, host=_MONGODB_DATABASE_HOST)


from mongoengine import *
conn = connect('venv1_7cl')
# put dbname in db & them import this `db` in all files, and access, db.collections
db = conn['venv1_7cl']

# SESSION_ENGINE = 'mongoengine.django.sessions'
# SESSION_SERIALIZER = 'mongoengine.django.sessions.BSONSerializer'

# MONGOENGINE_USER_DOCUMENT = 'mongoengine.django.auth.User'

# Added-


