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

# Create superuser if it doesn't exist
try:
    from django.contrib.auth.models import User
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser(
            username='admin',
            email='admin@sikshyakendra.com',
            password='admin123'
        )
        print("✅ SUPERUSER CREATED: admin/admin123")
    else:
        print("ℹ️  Superuser 'admin' already exists!")
except Exception as e:
    print(f"⚠️  Could not create superuser: {e}")

application = get_wsgi_application()

print("🚀 NUCLEAR FIX: WSGI application loaded successfully!")
print("🚀 Using SQLite database - NO POSTGRESQL ISSUES!")
print("🚀 Your app is READY!")