import os.path
import sys

# Include apps on the path
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
sys.path.insert(0, os.path.join(PROJECT_ROOT, "apps"))

# URL prefix for CSS, JavaScript and images used by the Django admin.
# Use a trailing slash, and to have this be different from MEDIA_URL
# For integration with staticfiles, this should be  STATIC_URL + 'admin/'.
# Make it different to not host on CDN
ADMIN_MEDIA_PREFIX = '/static-local/admin/'

ADMIN_MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'static-local', 'admin')

# People who get code error notifications when DEBUG=False
ADMINS = (('__PROJECT_NAME__ administrator', '__ADMIN_EMAIL__'),)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_ROOT, 'dev.db'),
    }
}

# Never deploy a site into production with DEBUG turned on!
DEBUG = True

# Address to use for various automated correspondence from the site manager(s).
DEFAULT_FROM_EMAIL = '__ADMIN_EMAIL__'

# Set the subject prefix for email messages sent to admins and managers
EMAIL_SUBJECT_PREFIX = '[__PROJECT_NAME__] '

# Enviroment (development, staging, test, production) affects the admin colors
ENVIRONMENT = 'development' # admin links will be green

# Maximum size (in bytes) before an upload gets streamed to the file system.
FILE_UPLOAD_MAX_MEMORY_SIZE = 5242880

# List of locations of the fixture data files, in search order
FIXTURE_DIRS = ()

# The Site Title of your Admin-Interface. Change this instead of changing index.html
GRAPPELLI_ADMIN_TITLE = "__PROJECT_NAME__"

# A tuple of strings designating all the enabled applications
INSTALLED_APPS = (
    'grappelli',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.humanize',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'ff0000', # load django-admin commands, initial fixtures, ..
)

# A tuple of IP addresses that see debug comments, when DEBUG is True
INTERNAL_IPS = ('0.0.0.0', '127.0.0.1',)

# The language code for this installation
LANGUAGE_CODE = 'en-us'

# If login is successful, the view redirects to the URL specified in next.
# If next isn't provided, it redirects to settings.LOGIN_REDIRECT_URL
# (which defaults to /accounts/profile/).
LOGIN_REDIRECT_URL = '/admin'

# Who should get broken-link notifications when SEND_BROKEN_LINK_EMAILS=True
MANAGERS = ADMINS

# Absolute path to the directory that holds stored files.
MEDIA_ROOT = os.path.join(PROJECT_ROOT, '..', 'uploads')

# URL that handles the media served from MEDIA_ROOT (must end in a slash)
MEDIA_URL = '/uploads/'

# A tuple of middleware classes to use
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'ff0000.middleware.XUACompatibleMiddleware'
)

# Number of digits grouped together on the integer part of a number
NUMBER_GROUPING = 3

# The full Python import path to the root URLconf
ROOT_URLCONF = 'urls'

# Seed for secret-key hashing algorithms
SECRET_KEY = '__SECRET_KEY_SEED__'

# Whether files other than .html should be returned with the correct MIME type
SET_MIMETYPE = True

# The ID of the current site in the django_site database table
SITE_ID = 1

# Absolute path to the directory where collectstatic will collect static files
STATIC_ROOT = ''

# URL to use when referring to static files located in STATIC_ROOT
STATIC_URL = '/static/'

# Additional locations the staticfiles app will traverse
STATICFILES_DIRS = (os.path.join(PROJECT_ROOT, 'static'),)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
    'ff0000.context_processors.settings',
)

# Display a detailed report for any TemplateSyntaxError.
TEMPLATE_DEBUG = DEBUG

# List of locations of the template source files, in search order
TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates'),
)

# A tuple of template loader classes, specified as strings
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

# The time zone for this installation
TIME_ZONE = 'America/Los_Angeles'

# Output the "Etag" header. This saves bandwidth but slows down performance
USE_ETAGS = False

# Display numbers using a thousand separator
USE_THOUSAND_SEPARATOR = True

# Enable Django's internationalization system
USE_I18N = True

# Display numbers and dates using the format of the current locale
USE_L10N = True
