from settings import INSTALLED_APPS


ALLOWED_HOSTS = ['']
INTERNAL_IPS = ('127.0.0.1')

DEBUG = False
SECRET_KEY = ''
CSRF_COOKIE_SECURE = True


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': ''
    }
}
