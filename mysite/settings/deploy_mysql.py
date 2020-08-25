from .base import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dongguk_food',
        'USER': 'root',
        'PASSWORD': 'elwkdldjhd12',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

DISQUS_SHORTNAME = 'donnguk-food'
DISQUS_MY_DOMAIN = 'http://somefood.pythonanywhere.com'