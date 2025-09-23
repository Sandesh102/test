#!/usr/bin/env python
"""
Check if admin user exists and create if needed
"""

import os
import sys
import django
from pathlib import Path

print("🔍 CHECKING ADMIN USER")
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
    
    print("\n2. Testing database connection...")
    from django.db import connection
    with connection.cursor() as cursor:
        cursor.execute("SELECT 1")
        result = cursor.fetchone()
        print(f"✅ Database connection: {result}")
    
    print("\n3. Checking User model...")
    from django.contrib.auth.models import User
    user_count = User.objects.count()
    print(f"✅ Total users: {user_count}")
    
    print("\n4. Checking for admin user...")
    admin_users = User.objects.filter(username='admin')
    if admin_users.exists():
        admin = admin_users.first()
        print(f"✅ Admin user exists: {admin.username}")
        print(f"✅ Admin email: {admin.email}")
        print(f"✅ Admin staff: {admin.is_staff}")
        print(f"✅ Admin superuser: {admin.is_superuser}")
        print(f"✅ Admin active: {admin.is_active}")
        
        # Test password
        if admin.check_password('admin123'):
            print("✅ Admin password works!")
        else:
            print("❌ Admin password does NOT work!")
            print("🔧 Resetting password...")
            admin.set_password('admin123')
            admin.save()
            print("✅ Password reset to 'admin123'")
    else:
        print("❌ No admin user found!")
        print("🔧 Creating admin user...")
        
        # Delete any existing admin users first
        User.objects.filter(username='admin').delete()
        
        # Create new admin user
        admin = User.objects.create_superuser(
            username='admin',
            email='admin@test.com',
            password='admin123'
        )
        print(f"✅ Admin user created: {admin.username}")
        print(f"✅ Admin email: {admin.email}")
        print(f"✅ Admin staff: {admin.is_staff}")
        print(f"✅ Admin superuser: {admin.is_superuser}")
        print(f"✅ Admin active: {admin.is_active}")
    
    print("\n5. Final verification...")
    admin = User.objects.get(username='admin')
    if admin.check_password('admin123'):
        print("✅ FINAL VERIFICATION: Password works!")
        print("✅ Admin user is ready!")
    else:
        print("❌ FINAL VERIFICATION: Password still doesn't work!")
    
    print("\n6. Testing login...")
    from django.contrib.auth import authenticate
    user = authenticate(username='admin', password='admin123')
    if user:
        print("✅ LOGIN TEST: Authentication successful!")
        print(f"✅ User: {user.username}")
        print(f"✅ Staff: {user.is_staff}")
        print(f"✅ Superuser: {user.is_superuser}")
    else:
        print("❌ LOGIN TEST: Authentication failed!")
    
    print("\n🎉 ADMIN USER CHECK COMPLETE!")
    
except Exception as e:
    print(f"\n💥 ERROR: {e}")
    import traceback
    traceback.print_exc()

if __name__ == "__main__":
    print("Check complete!")
