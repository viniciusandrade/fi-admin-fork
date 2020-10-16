# coding: utf-8
# Django settings for fi-admin project.
import os
import sys
import re
import logging

DEBUG = int(os.environ.get("DEBUG", 0))
DEBUG_TOOLBAR = int(os.environ.get("DEBUG_TOOLBAR", 0))

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

PROJECT_ROOT_PATH = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

DATABASES = {
     'default': {
         'ENGINE': os.environ.get("DATABASE_ENGINE", 'django.db.backends.sqlite3'),
         'NAME': os.environ.get("DATABASE_NAME", 'database.db'),
         'USER': os.environ.get("DATABASE_USER"),
         'PASSWORD': os.environ.get("DATABASE_PASSWORD"),
         'HOST': os.environ.get("DATABASE_HOST"),
         'PORT': os.environ.get("DATABASE_PORT"),
     },
    'decs_portal': {
        'ENGINE': os.environ.get("DATABASE_DECS_ENGINE"),
        'NAME': os.environ.get("DATABASE_DECS_NAME"),
        'USER': os.environ.get("DATABASE_DECS_USER"),
        'PASSWORD': os.environ.get("DATABASE_DECS_PASSWORD"),
        'HOST': os.environ.get("DATABASE_DECS_HOST"),
        'PORT': os.environ.get("DATABASE_DECS_PORT"),
    },
 }


# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Sao_Paulo'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'pt-BR'

LANGUAGES = (
    ('en', u'English'),
    ('pt-BR', u'Português'),
    ('es', u'Espanhol'),
)

LOCALE_PATHS =(
    os.path.join(PROJECT_ROOT_PATH, 'locale'),
)

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT_PATH, 'uploads')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/uploads/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = os.path.join(PROJECT_ROOT_PATH, 'static_files')

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_ROOT_PATH, 'static'),
    #os.path.join(PROJECT_ROOT_PATH, 'uploads'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = os.environ.get("SECRET_KEY")

DATE_INPUT_FORMATS = ('%d/%m/%Y')

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',

    'utils.context_processors.additional_user_info',
    'utils.context_processors.django_settings',
)


MIDDLEWARE_CLASSES = [
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'log.middleware.WhodidMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'fi-admin.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'fi-admin.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_ROOT_PATH, 'templates'),
)

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Django admin
    'django.contrib.admin',

    'haystack',
    'tastypie',
    'rosetta',
    'form_utils',
    'tinymce',

    'biremelogin',

    'api',
    'dashboard',
    'main',
    'events',
    'suggest',
    'error_reporting',
    'multimedia',
    'title',
    'biblioref',
    'leisref',
    'institution',
    'oer',
    'reports',
    'utils',
    'attachments',
    'help',
    'log',
    'text_block',
    'database',
    'classification',
    'thesaurus',
]

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


HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': os.environ.get("HAYSTACK_CONNECTION_ENGINE"),
        'URL': os.environ.get("HAYSTACK_CONNECTION_URL"),
    },
}

CACHES = {
    'default': {
        'BACKEND': os.environ.get("CACHE_BACKEND"),
        'LOCATION': os.environ.get("CACHE_LOCATION"),
    }
}

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.MD5PasswordHasher',
)

AUTHENTICATION_BACKENDS = (
    'biremelogin.authenticate.EmailModelBackend',
)

TINYMCE_JS_URL = "/static/js/tinymce/tinymce.min.js"

TINYMCE_DEFAULT_CONFIG = {
    'plugins': 'link table code',
    'theme': "modern",
    'menubar': False,
    'toolbar': 'undo redo | styleselect | bold italic | alignleft aligncenter alignright justify alignjustify | '
               'bullist numlist outdent indent | link image | table | code ',
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 10,
}

# for settings_context_processor
TEMPLATE_VISIBLE_SETTINGS = (
    'GOOGLE_ANALYTICS_ID',
    'SITE_URL'
)

# don't registry changes at specific fields on audit log (ex. control fields)
EXCLUDE_AUDITLOG_FIELDS = ('content_type', 'object_id', 'reference_title',
                           'literature_type', 'code', 'short_url')

TEST_RUNNER = 'django.test.runner.DiscoverRunner'

# set permissions after file upload (444 read only file for security reasons)
FILE_UPLOAD_PERMISSIONS = 0444

# set max upload size
# 10MB - 10485760
MAX_UPLOAD_SIZE = "73400320" #70MB

##### FI-ADMIN SETTINGS ####

ITEMS_PER_PAGE = 20
LOGIN_URL = '/login/'
DEFAULT_COOPERATIVE_CENTER = 'BR1.1'
BIREMELOGIN_SERVICE = ''

EXPOSE_API_ONLY = int(os.environ.get("EXPOSE_API_ONLY"), 0)
MAX_EXPORT_API_LIMIT = os.environ.get("MAX_EXPORT_API_LIMIT", 100)

HAYSTACK_SIGNAL_PROCESSOR = os.environ.get("HAYSTACK_SIGNAL_PROCESSOR")

SITE_URL = os.environ.get("SITE_URL")
BIREMELOGIN_BASE_URL = os.environ.get("BIREMELOGIN_BASE_URL")
VIEW_DOCUMENTS_BASE_URL = os.environ.get("VIEW_DOCUMENTS_BASE_URL")

SEARCH_SERVICE_URL = os.environ.get("SEARCH_SERVICE_URL")
DECS_LOOKUP_SERVICE = os.environ.get("DECS_LOOKUP_SERVICE")
GOOGLE_ANALYTICS_ID = os.environ.get("GOOGLE_ANALYTICS_ID")
DEDUP_SERVICE_URL = os.environ.get("DEDUP_SERVICE_URL")
DEDUP_ARTICLE_DETAIL = os.environ.get("DEDUP_ARTICLE_DETAIL")
DEDUP_PUT_URL = os.environ.get("DEDUP_PUT_URL")
DECS_HIGHLIGHTER_URL = os.environ.get("DECS_HIGHLIGHTER_URL")

RECAPTCHA_PRIVATE_KEY = os.environ.get("RECAPTCHA_PRIVATE_KEY")
GOOGLE_MAPS_APIKEY = os.environ.get("GOOGLE_MAPS_APIKEY")

FULLTEXT_SEARCH = os.environ.get("FULLTEXT_SEARCH")

ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS")

EMAIL_HOST = os.environ.get("EMAIL_HOST")
EMAIL_PORT = os.environ.get("EMAIL_PORT")
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")
EMAIL_FROM = os.environ.get("EMAIL_FROM")


# Enable debug_toolbar bypass INTERNAL_IPS parameter
DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': lambda _request: DEBUG_TOOLBAR
}


if DEBUG_TOOLBAR:
    INSTALLED_APPS.append('debug_toolbar')

    debug_toolbar_middleware = ['debug_toolbar.middleware.DebugToolbarMiddleware', 'fi-admin.utils.NonHtmlDebugToolbarMiddleware']
    MIDDLEWARE_CLASSES.extend(debug_toolbar_middleware)

if 'test' in sys.argv:
    logging.disable(logging.CRITICAL)
    DEBUG = False
    TEMPLATE_DEBUG = False
    TESTS_IN_PROGRESS = True
    MIGRATION_MODULES = DisableMigrations()
    HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.BaseSignalProcessor'


class DisableMigrations(object):
    def __contains__(self, item):
        return True

    def __getitem__(self, item):
        return "notmigrations"
