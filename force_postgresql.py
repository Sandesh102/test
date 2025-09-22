#!/usr/bin/env python
"""
FORCE POSTGRESQL - This will ensure PostgreSQL is used
"""

import os
import sys

print("🐘 FORCING POSTGRESQL DATABASE!")
print("=" * 50)

# Force PostgreSQL settings
os.environ['DJANGO_SETTINGS_MODULE'] = 'std_portal.production'
os.environ['FORCE_POSTGRESQL'] = 'TRUE'
os.environ['NO_SQLITE'] = 'TRUE'

print("✅ Environment set for PostgreSQL!")
print("✅ Settings module: std_portal.production")
print("✅ PostgreSQL forced!")

# Set up Django
import django
from pathlib import Path

project_dir = Path(__file__).parent
sys.path.insert(0, str(project_dir))

django.setup()

from django.contrib.auth.models import User
from django.db import connection

def create_postgresql_admin():
    print("\n🐘 CREATING POSTGRESQL ADMIN USER")
    print("=" * 40)
    
    try:
        # Test database connection
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            result = cursor.fetchone()
            print(f"✅ PostgreSQL connection test: {result}")
        
        # Check if admin exists
        if User.objects.filter(username='admin').exists():
            admin = User.objects.get(username='admin')
            print(f"✅ Admin user exists: {admin.username}")
            
            # Verify password
            if admin.check_password('admin123'):
                print("✅ Password verification: SUCCESS!")
            else:
                print("⚠️ Resetting password...")
                admin.set_password('admin123')
                admin.save()
                print("✅ Password reset: SUCCESS!")
            
            # Ensure permissions
            admin.is_staff = True
            admin.is_superuser = True
            admin.is_active = True
            admin.save()
            print("✅ Admin permissions verified!")
            
        else:
            print("Creating new admin user...")
            admin = User.objects.create_superuser(
                username='admin',
                email='admin@sikshyakendra.com',
                password='admin123'
            )
            print(f"✅ Admin user created: {admin.username}")
        
        print("\n🎉 POSTGRESQL ADMIN USER READY!")
        print("Username: admin")
        print("Password: admin123")
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = create_postgresql_admin()
    if success:
        print("\n🚀 POSTGRESQL SETUP COMPLETE!")
        sys.exit(0)
    else:
        print("\n💥 POSTGRESQL SETUP FAILED!")
        sys.exit(1)
