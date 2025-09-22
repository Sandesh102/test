#!/usr/bin/env python
"""
Debug 500 error - Check what's causing the server error
"""

import os
import sys
import django
from pathlib import Path

print("🔍 DEBUGGING 500 ERROR")
print("=" * 50)

# Add the project directory to Python path
project_dir = Path(__file__).parent
sys.path.insert(0, str(project_dir))

# Set up Django with production settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'std_portal.production')

try:
    print("1. Setting up Django...")
    django.setup()
    print("✅ Django setup successful")
    
    print("\n2. Testing database connection...")
    from django.db import connection
    with connection.cursor() as cursor:
        cursor.execute("SELECT 1")
        result = cursor.fetchone()
        print(f"✅ Database connection: {result}")
    
    print("\n3. Testing User model...")
    from django.contrib.auth.models import User
    user_count = User.objects.count()
    print(f"✅ User model works: {user_count} users")
    
    print("\n4. Testing admin user...")
    admin_users = User.objects.filter(username='admin')
    if admin_users.exists():
        admin = admin_users.first()
        print(f"✅ Admin user exists: {admin.username}")
        print(f"✅ Admin staff: {admin.is_staff}")
        print(f"✅ Admin superuser: {admin.is_superuser}")
        
        # Test password
        if admin.check_password('admin123'):
            print("✅ Admin password works!")
        else:
            print("❌ Admin password does NOT work!")
    else:
        print("❌ No admin user found!")
    
    print("\n5. Testing Django settings...")
    from django.conf import settings
    print(f"✅ DEBUG: {settings.DEBUG}")
    print(f"✅ DATABASE ENGINE: {settings.DATABASES['default']['ENGINE']}")
    print(f"✅ ALLOWED_HOSTS: {settings.ALLOWED_HOSTS}")
    
    print("\n6. Testing URL patterns...")
    from django.urls import reverse
    try:
        admin_url = reverse('admin:index')
        print(f"✅ Admin URL: {admin_url}")
    except Exception as e:
        print(f"❌ Admin URL error: {e}")
    
    print("\n7. Testing static files...")
    print(f"✅ STATIC_URL: {settings.STATIC_URL}")
    print(f"✅ STATIC_ROOT: {settings.STATIC_ROOT}")
    
    print("\n🎉 ALL TESTS PASSED - NO 500 ERROR CAUSE FOUND!")
    
except Exception as e:
    print(f"\n💥 ERROR FOUND: {e}")
    import traceback
    traceback.print_exc()
    
    # Check specific common issues
    print("\n🔍 CHECKING COMMON ISSUES:")
    
    # Check if database exists
    try:
        from django.db import connection
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
    except Exception as db_error:
        print(f"❌ Database error: {db_error}")
    
    # Check if migrations are needed
    try:
        from django.core.management import execute_from_command_line
        print("Checking migrations...")
    except Exception as migration_error:
        print(f"❌ Migration error: {migration_error}")
    
    # Check if static files are missing
    try:
        from django.contrib.staticfiles import finders
        static_files = finders.find('admin/css/base.css')
        print(f"Static files: {static_files}")
    except Exception as static_error:
        print(f"❌ Static files error: {static_error}")

if __name__ == "__main__":
    print("Debug complete!")
