import os
import dj_database_url
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SECRET_KEY = '4ekx+7c2=(^g@7@$)=#(bj$v)q2i5uoiv^h+7*8hl*v$@gp^^z'

DEBUG = bool(os.environ.get('DEMO_DEBUG', False))
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = (
    'django.contrib.staticfiles',
    'flickr_pony',
    'ui'
)

MIDDLEWARE_CLASSES = (
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.common.CommonMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'wsgi.application'
DATABASES = {'default': dj_database_url.config()}

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

FLICKR_STORAGE_OPTIONS = {
    'api_key': os.environ.get('FLICKR_API_KEY'),
    'user_id': os.environ.get('FLICKR_USER_ID')
}
