import os
from pathlib import Path

from django.core.management.utils import get_random_secret_key
from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parent.parent

path_to_env = os.path.join(BASE_DIR, '..', 'infra', '.env')

load_dotenv(path_to_env)

SECRET_KEY = os.getenv('SECRET_KEY', default=get_random_secret_key())

DEBUG = True
ALLOWED_HOSTS = ('127.0.0.1',)

INSTALLED_APPS = (
    'django.forms',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'phonenumber_field',
    'account.apps.AccountConfig',
    'core.apps.CoreConfig',
    'order.apps.OrderConfig',
    'api.apps.ApiConfig',
    'sorl.thumbnail',
)

MIDDLEWARE = (
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'freelance_site.urls'

TEMPLATES = (
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': (os.path.join(BASE_DIR, 'templates'),),
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': (
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'core.context_processors.user_processors.login_form',
                'core.context_processors.user_processors.reset_form',
                'core.context_processors.user_processors.get_user_picture',
            ),
        },
    },
)

WSGI_APPLICATION = 'freelance_site.wsgi.application'

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

DATABASES = {
    'default': {
        'ENGINE': os.getenv('DB_ENGINE',
                            default='django.db.backends.postgresql'),
        'NAME': os.getenv('POSTGRES_DB', default='YouBase'),
        'USER': os.getenv('POSTGRES_USER', default='YouName'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD', default='YouPassword'),
        'HOST': os.getenv('DB_HOST', default='localhost'),
        'PORT': os.getenv('DB_PORT', default='5432'),
        'TIME_ZONE': TIME_ZONE,
    }
}


REDIS_LOCATION = f'redis://{os.getenv('REDIS_HOST', default='localhost')}:{os.getenv('REDIS_PORT', default='6379')}'

CELERY_BROKER_URL = f'{REDIS_LOCATION}/0'
CELERY_RESULT_BACKEND = f'{REDIS_LOCATION}/0'
CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP = True
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 5 * 60
CELERY_ACCEPT_CONTENT = ('application/json',)
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'
CELERY_TIMEZONE = TIME_ZONE

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': REDIS_LOCATION,
    }
}

AUTH_PASSWORD_VALIDATORS = (
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
)

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
if DEBUG:
    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, 'static'),
        )
else:
    STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_URL = 'account:login'
LOGIN_REDIRECT_URL = '/account/'

AUTH_USER_MODEL = 'account.User'

YEARS_150_IN_DAYS = 54750

FORM_RENDERER = 'django.forms.renderers.TemplatesSetting'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DAYS_LIFE_ORDER = 30

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 15
}
