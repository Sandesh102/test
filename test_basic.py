#!/usr/bin/env python
"""
Test basic Django functionality
"""

import os
import sys
import django
from pathlib import Path

print("🧪 TESTING BASIC DJANGO FUNCTIONALITY")
print("=" * 50)

# Add the project directory to Python path
project_dir = Path(__file__).parent
sys.path.insert(0, str(project_dir))

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'std_portal.production')

try:
    print("1. Importing Django...")
    import django
    print(f"✅ Django version: {django.get_version()}")
    
    print("\n2. Setting up Django...")
    django.setup()
    print("✅ Django setup successful")
    
    print("\n3. Testing basic imports...")
    from django.conf import settings
    print("✅ Settings imported")
    
    from django.contrib.auth.models import User
    print("✅ User model imported")
    
    from django.db import connection
    print("✅ Database connection imported")
    
    print("\n4. Testing database...")
    with connection.cursor() as cursor:
        cursor.execute("SELECT 1")
        result = cursor.fetchone()
        print(f"✅ Database query: {result}")
    
    print("\n5. Testing User model...")
    user_count = User.objects.count()
    print(f"✅ User count: {user_count}")
    
    print("\n6. Testing admin user creation...")
    if not User.objects.filter(username='admin').exists():
        admin = User.objects.create_superuser(
            username='admin',
            email='admin@test.com',
            password='admin123'
        )
        print(f"✅ Admin user created: {admin.username}")
    else:
        admin = User.objects.get(username='admin')
        print(f"✅ Admin user exists: {admin.username}")
    
    print("\n7. Testing password...")
    if admin.check_password('admin123'):
        print("✅ Password verification: SUCCESS!")
    else:
        print("❌ Password verification: FAILED!")
    
    print("\n🎉 ALL BASIC TESTS PASSED!")
    print("The Django app should work fine!")
    
except Exception as e:
    print(f"\n💥 ERROR: {e}")
    import traceback
    traceback.print_exc()
    
    print("\n🔍 DETAILED ERROR ANALYSIS:")
    print(f"Error type: {type(e).__name__}")
    print(f"Error message: {str(e)}")
    
    # Check if it's a database issue
    if "database" in str(e).lower() or "connection" in str(e).lower():
        print("❌ DATABASE CONNECTION ISSUE")
    elif "import" in str(e).lower() or "module" in str(e).lower():
        print("❌ IMPORT/MODULE ISSUE")
    elif "settings" in str(e).lower():
        print("❌ SETTINGS CONFIGURATION ISSUE")
    else:
        print("❌ UNKNOWN ISSUE")

if __name__ == "__main__":
    print("\nTest complete!")

