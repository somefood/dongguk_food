from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dg_food_desktop',
        'USER': 'root',
        'PASSWORD' : 'tjrwn12',
        'HOST' : '192.168.42.100',
        'PORT': '3306',
        'OPTIONS' :{
            'init_command': 'SET sql_mode="STRICT_TRANS_TABLES"',
        }
    }
}
