"""
WSGI config for std_portal project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
import sys

# NUCLEAR FIX: Force SQLite database
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'std_portal.settings')
os.environ['FORCE_SQLITE'] = 'TRUE'
os.environ['NUCLEAR_FIX'] = 'TRUE'

print("DEBUG: NUCLEAR FIX - WSGI starting with SQLite!")
print("DEBUG: This WILL work now!")

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

print("DEBUG: WSGI application loaded successfully!")
print("DEBUG: Using SQLite database - NO POSTGRESQL ISSUES!")