"""
Production settings for PostgreSQL deployment
"""

from .settings import *
import os

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Database configuration for PostgreSQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'student_portal_db_a2e2',
        'USER': 'student_portal_db_a2e2_user',
        'PASSWORD': 'xP59H1q1uG9d3xwjTxMBRc90fhE86HOd',
        'HOST': 'dpg-d380kkodl3ps73au33vg-a.oregon-postgres.render.com',
        'PORT': '5432',
    }
}

# Allowed hosts for production
ALLOWED_HOSTS = [
    'student-portal-if4i.onrender.com',
    'test-hvdl.onrender.com',
    'localhost',
    '127.0.0.1',
    '0.0.0.0',
    '*'
]

# Static files configuration
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Media files configuration
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Security settings
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'

# Email configuration (if needed)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', 'your-email@gmail.com')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', 'your-app-password')

# Site configuration
SITE_DOMAIN = os.environ.get('SITE_DOMAIN', 'student-portal.onrender.com')
SITE_NAME = os.environ.get('SITE_NAME', 'Sikshya Kendra')

