#!/usr/bin/env python
"""
Force create admin user - Ultimate solution
"""

import os
import sys
import django
from pathlib import Path

print("🚀 FORCE ADMIN CREATION")
print("=" * 50)

# Add the project directory to Python path
project_dir = Path(__file__).parent
sys.path.insert(0, str(project_dir))

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'std_portal.settings')

try:
    print("1. Setting up Django...")
    django.setup()
    print("✅ Django setup successful")
    
    print("\n2. Testing database...")
    from django.db import connection
    with connection.cursor() as cursor:
        cursor.execute("SELECT 1")
        result = cursor.fetchone()
        print(f"✅ Database connection: {result}")
    
    print("\n3. Force creating admin user...")
    from django.contrib.auth.models import User
    
    # Delete any existing admin users
    User.objects.filter(username='admin').delete()
    print("✅ Deleted existing admin users")
    
    # Create new admin user
    admin = User.objects.create_superuser(
        username='admin',
        email='admin@test.com',
        password='admin123'
    )
    print(f"✅ Admin user created: {admin.username}")
    
    # Force set all required flags
    admin.is_staff = True
    admin.is_superuser = True
    admin.is_active = True
    admin.save()
    print("✅ Admin flags set: staff=True, superuser=True, active=True")
    
    print("\n4. Testing password...")
    if admin.check_password('admin123'):
        print("✅ Password verification: SUCCESS!")
    else:
        print("❌ Password verification: FAILED!")
        # Reset password
        admin.set_password('admin123')
        admin.save()
        print("✅ Password reset to 'admin123'")
    
    print("\n5. Testing authentication...")
    from django.contrib.auth import authenticate
    user = authenticate(username='admin', password='admin123')
    if user:
        print("✅ Authentication test: SUCCESS!")
        print(f"✅ User: {user.username}")
        print(f"✅ Staff: {user.is_staff}")
        print(f"✅ Superuser: {user.is_superuser}")
        print(f"✅ Active: {user.is_active}")
    else:
        print("❌ Authentication test: FAILED!")
    
    print("\n6. Final verification...")
    admin = User.objects.get(username='admin')
    print(f"✅ Final admin user: {admin.username}")
    print(f"✅ Final staff: {admin.is_staff}")
    print(f"✅ Final superuser: {admin.is_superuser}")
    print(f"✅ Final active: {admin.is_active}")
    
    print("\n🎉 ADMIN USER FORCE CREATION COMPLETE!")
    print("✅ Username: admin")
    print("✅ Password: admin123")
    print("✅ Ready for login!")
    
except Exception as e:
    print(f"\n💥 ERROR: {e}")
    import traceback
    traceback.print_exc()

if __name__ == "__main__":
    print("Force admin creation complete!")
