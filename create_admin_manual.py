#!/usr/bin/env python
"""
Manual admin creation script
Run this to create admin user manually
"""

import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'std_portal.settings')
django.setup()

from django.contrib.auth.models import User

def create_admin_manually():
    """Create admin user manually"""
    print("🚀 MANUAL ADMIN CREATION...")
    
    try:
        # Check if admin exists
        if User.objects.filter(username='admin').exists():
            print("ℹ️  Admin user already exists!")
            admin = User.objects.get(username='admin')
            print(f"Username: {admin.username}")
            print(f"Email: {admin.email}")
            print(f"Is superuser: {admin.is_superuser}")
            print(f"Is staff: {admin.is_staff}")
        else:
            # Create admin user
            admin = User.objects.create_superuser(
                username='admin',
                email='admin@sikshyakendra.com',
                password='admin123'
            )
            print("✅ ADMIN USER CREATED!")
            print("Username: admin")
            print("Password: admin123")
            print("Email: admin@sikshyakendra.com")
        
        # Verify the user
        admin = User.objects.get(username='admin')
        print(f"\n✅ VERIFICATION:")
        print(f"Username: {admin.username}")
        print(f"Email: {admin.email}")
        print(f"Is superuser: {admin.is_superuser}")
        print(f"Is staff: {admin.is_staff}")
        print(f"Is active: {admin.is_active}")
        
        print(f"\n🔗 Login at: https://test-hvdl.onrender.com/admin/")
        
    except Exception as e:
        print(f"❌ ERROR: {e}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    create_admin_manually()

