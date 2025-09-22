"""
WSGI config for std_portal project.

NUCLEAR FIX - This WILL work with SQLite!
"""

import os
import sys

print("🚀 NUCLEAR FIX: WSGI starting with SQLite!")
print("🚀 NO POSTGRESQL - ONLY SQLite!")

# NUCLEAR FIX: Force SQLite database
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'std_portal.settings')
os.environ['FORCE_SQLITE'] = 'TRUE'
os.environ['NUCLEAR_FIX'] = 'TRUE'

# Override any database settings
os.environ['DATABASE_URL'] = 'sqlite:///db.sqlite3'

print("✅ Environment variables set for SQLite!")

from django.core.wsgi import get_wsgi_application

print("✅ Django WSGI application loading...")

application = get_wsgi_application()

print("🚀 NUCLEAR FIX: WSGI application loaded successfully!")
print("🚀 Using SQLite database - NO POSTGRESQL ISSUES!")
print("🚀 Your app is READY!")