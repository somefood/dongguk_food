from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dg_food_db',
        'USER': 'root',
        'PASSWORD' : 'tjrwn12',
        'HOST' : 'localhost',
        'PORT': '3306',
        'OPTIONS' :{
            'init_command': 'SET sql_mode="STRICT_TRANS_TABLES"',
        }
    }
}
