import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG

SITE_ROOT = os.path.abspath(os.path.dirname(__file__))
PARENT_FOLDER = os.path.join(SITE_ROOT,os.pardir)

ADMINS = (
    ("Crowdfunding", "crowdfunding@mailinator.com"),
)

MANAGERS = ADMINS

if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': os.path.join(PARENT_FOLDER, "db.sqlite3"),
            'USER': '',
            'PASSWORD': '',
            'HOST': '',# Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
            'PORT': '',# Set to empty string for default.
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE" : "django.db.backends.postgresql_psycopg2",
            "NAME" : "together",
            "USER" : "together_user",
            "PASSWORD" : "together_password",
            "HOST" : "",
            "PORT" : ""
        }
    }

ALLOWED_HOSTS = []

TIME_ZONE = 'America/Santiago'

LANGUAGE_CODE = 'es-CL'

SITE_ID = 1

USE_I18N = True


USE_L10N = True

USE_TZ = True

MEDIA_ROOT = os.path.join(PARENT_FOLDER, '/user_uploads')

MEDIA_URL = '/user_uploads/'

STATIC_ROOT = os.path.join(SITE_ROOT, '/static_root')

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(SITE_ROOT, "static"),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'egb2(g$8qr(2ofz3dqt*kyyhth)^&8^fq)9dshhhm5$#2gvxoe'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'crowdfunding.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'crowdfunding.wsgi.application'

TEMPLATE_DIRS = (
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'together',
)

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
