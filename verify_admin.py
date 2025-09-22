#!/usr/bin/env python
"""
Verify admin user exists and can login
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

def verify_admin():
    print("🔍 VERIFYING ADMIN USER")
    print("=" * 40)
    
    try:
        # Check if admin exists
        admin_users = User.objects.filter(username='admin')
        
        if admin_users.exists():
            admin = admin_users.first()
            print(f"✅ Admin user found: {admin.username}")
            print(f"✅ Email: {admin.email}")
            print(f"✅ Staff: {admin.is_staff}")
            print(f"✅ Superuser: {admin.is_superuser}")
            print(f"✅ Active: {admin.is_active}")
            
            # Test password
            if admin.check_password('admin123'):
                print("✅ Password verification: SUCCESS!")
                print("\n🎉 ADMIN USER IS READY!")
                print("Username: admin")
                print("Password: admin123")
                return True
            else:
                print("❌ Password verification: FAILED!")
                return False
        else:
            print("❌ No admin user found!")
            return False
            
    except Exception as e:
        print(f"❌ Error verifying admin: {e}")
        return False

if __name__ == "__main__":
    verify_admin()

