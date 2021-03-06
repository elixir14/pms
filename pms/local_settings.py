DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'pm',  # database name
        'USER': 'postgres',  # database username
        'PASSWORD': 'root',  # database password
        'HOST': '127.0.0.1',  # database server
        'PORT': '5432',  # database serer port. 5432 is default port of postgresql.
    }
}

DEV_DEBUG = True

MEDIA_URL = 'http://127.0.0.1:8000/media/'

EMAIL_HOST = ''
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 587
EMAIL_USE_TLS = True
