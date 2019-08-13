"""
Django settings for test_platform project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(1, os.path.join(BASE_DIR, 'exta_apps'))
sys.path.insert(1, os.path.join(BASE_DIR, 'apps'))
sys.path.insert(1, os.path.join(BASE_DIR, 'decodetools'))
sys.path.insert(1, os.path.join(BASE_DIR, 'test_platform'))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*@#fk*9ay6j)@6@asfxug-azgjvcguh+ue7q-03fa@3r*&faj_'

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
DEBUG = True


ALLOWED_HOSTS = ['*',]
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'test_platform',
    'users',
    'project',
    'module',
    'testcase',
    'xadmin',
    'crispy_forms',
    'captcha',
    'mock',
	'testtask',
	'tools',
	'locustmanager',
    'pyunitest',
	'apk',
    # https://django-simple-captcha.readthedocs.io/en/latest/usage.html
]

MIDDLEWARE = [
	'django.middleware.security.SecurityMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'test_platform.urls'

TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [os.path.join(BASE_DIR, "templates")],
		'APP_DIRS': True,
		'OPTIONS': {
			'context_processors': [
				'django.template.context_processors.debug',
				'django.template.context_processors.request',
				'django.contrib.auth.context_processors.auth',
				'django.contrib.messages.context_processors.messages',
			],
		},
	},
]

WSGI_APPLICATION = 'test_platform.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
# DATABASES = {
# 	'default': {
# 		'ENGINE': 'django.db.backends.mysql',
# 		'NAME': "apitestserver",
# 		'HOST': "127.0.0.1",
# 		# 'HOST': "172.31.1.12",
# 		'PORT': 3306,
# 		'USER': "qa",
# 		'PASSWORD': "qatest",
# 		# 'OPTIONS': {
# 		#     'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
# 		# },
# 	}
# }


# MySQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': BASE_DIR + '/my.cnf',
        },
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://your_host_ip:6379',
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
             "PASSWORD": "yoursecret",
        },
    },
}
REDIS_TIMEOUT=7*24*60*60
CUBES_REDIS_TIMEOUT=60*60
NEVER_REDIS_TIMEOUT=365*24*60*60

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
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
]

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'zh-hans'
TIME_ZONE = 'Asia/Shanghai'
USE_I18N = True
USE_L10N = True
# 数据库取本地时间
USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
	os.path.join(BASE_DIR, "static"),
]
#文件上传
FILE_LOCUSTROOT = os.path.join("/export/server/pref/locust","uploads")
FILE_APK = os.path.join("/export/server/pref/apk","uploads")
FILE_PYROOT = os.path.join("/export/server/pref/py_unittest","uploads")
PYTHON_UNITTEST_JENKINS_DIR = "/export/server/pref/python_unittest/interface_apitestByunitest_jenkins/tests/"
#扩展目录 test_platform/apps/testtask/extend/
EXTEND_DIR = os.path.join(BASE_DIR,"apps/testtask/extend/")


APPEND_SLASH = False
#  UserProfile 覆盖了 django 内置的 user 表
AUTH_USER_MODEL = 'users.UserProfile'


# 验证码图片大小
CAPTCHA_IMAGE_SIZE = (100, 35)
CAPTCHA_BACKGROUND_COLOR = '#ffffff'
CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.random_char_challenge'  # 图片中的文字为随机英文字母，如 mdsh
# CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.math_challenge'    # 图片中的文字为数字表达式，如1+2=</span>
CAPTCHA_LENGTH = 4  # 字符个数
CAPTCHA_TIMEOUT = 1  # 超时(minutes)
