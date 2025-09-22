#!/usr/bin/env python
"""
Debug script to check what's happening with admin user
"""

import os
import sys
import django
from pathlib import Path

# Add the project directory to Python path
project_dir = Path(__file__).parent
sys.path.insert(0, str(project_dir))

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'std_portal.settings')
django.setup()

from django.contrib.auth.models import User
from django.db import connection

def debug_admin():
    print("🔍 DEBUGGING ADMIN USER ISSUE")
    print("=" * 50)
    
    try:
        # Check all users
        all_users = User.objects.all()
        print(f"Total users in database: {all_users.count()}")
        
        for user in all_users:
            print(f"User: {user.username}, Staff: {user.is_staff}, Superuser: {user.is_superuser}, Active: {user.is_active}")
        
        # Check specifically for admin
        admin_users = User.objects.filter(username='admin')
        print(f"\nAdmin users found: {admin_users.count()}")
        
        if admin_users.exists():
            admin = admin_users.first()
            print(f"Admin details:")
            print(f"  - Username: {admin.username}")
            print(f"  - Email: {admin.email}")
            print(f"  - Staff: {admin.is_staff}")
            print(f"  - Superuser: {admin.is_superuser}")
            print(f"  - Active: {admin.is_active}")
            print(f"  - Password hash: {admin.password[:50]}...")
            
            # Test password
            if admin.check_password('admin123'):
                print("✅ Password 'admin123' works!")
            else:
                print("❌ Password 'admin123' does NOT work!")
                
                # Try other common passwords
                for pwd in ['admin', 'password', '123456', 'admin123!']:
                    if admin.check_password(pwd):
                        print(f"✅ Password '{pwd}' works!")
                        break
                else:
                    print("❌ No common passwords work!")
        else:
            print("❌ No admin user found!")
            
        # Check database file
        db_path = os.path.join(project_dir, 'db.sqlite3')
        print(f"\nDatabase file exists: {os.path.exists(db_path)}")
        if os.path.exists(db_path):
            print(f"Database file size: {os.path.getsize(db_path)} bytes")
            
        # Check if we can create a user
        print("\nTesting user creation...")
        try:
            test_user = User.objects.create_user(
                username='test123',
                email='test@test.com',
                password='test123'
            )
            print("✅ Can create users - Django ORM works")
            test_user.delete()
            print("✅ Test user deleted")
        except Exception as e:
            print(f"❌ Cannot create users: {e}")
            
    except Exception as e:
        print(f"💥 Debug failed: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    debug_admin()

