from .base import *

DEBUG = False

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST_USER = os.environ['EMAIL_HOST_USER']
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']

DISQUS_SHORTNAME = 'donnguk-food'
DISQUS_MY_DOMAIN = 'http://somefood.pythonanywhere.com'