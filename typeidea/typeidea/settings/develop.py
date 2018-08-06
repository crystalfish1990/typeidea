# coding:utf-8

from .base import *  # NOQA

DEBUG = True

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # },

    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'typeidea',
        'USER': 'root',
        'PASSWORD': 'MyNewPass4!',
        'PORT': '3306',
        'HOST': '10.1.1.224',
    },
}