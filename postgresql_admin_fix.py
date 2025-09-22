#!/usr/bin/env python
"""
PostgreSQL Admin Fix - Create admin user for PostgreSQL deployment
"""

import os
import sys
import django
from pathlib import Path

# Add the project directory to Python path
project_dir = Path(__file__).parent
sys.path.insert(0, str(project_dir))

# Set up Django with production settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'std_portal.production')
django.setup()

from django.contrib.auth.models import User
from django.db import transaction

def create_postgresql_admin():
    print("🐘 POSTGRESQL ADMIN CREATION STARTED")
    print("=" * 50)
    
    try:
        # Check if admin user already exists
        if User.objects.filter(username='admin').exists():
            admin_user = User.objects.get(username='admin')
            print(f"Admin user already exists: {admin_user.username}")
            
            # Verify password
            if admin_user.check_password('admin123'):
                print("✅ Password verification: SUCCESS!")
            else:
                print("⚠️ Password verification: FAILED - Resetting password")
                admin_user.set_password('admin123')
                admin_user.save()
                print("✅ Password reset: SUCCESS!")
            
            # Ensure user is staff and superuser
            if not admin_user.is_staff:
                admin_user.is_staff = True
                admin_user.save()
                print("✅ Staff status: ENABLED")
            
            if not admin_user.is_superuser:
                admin_user.is_superuser = True
                admin_user.save()
                print("✅ Superuser status: ENABLED")
            
            print("=== POSTGRESQL ADMIN USER VERIFICATION COMPLETE ===")
            return True
        
        # Create new admin user
        with transaction.atomic():
            admin_user = User.objects.create_user(
                username='admin',
                email='admin@example.com',
                password='admin123',
                is_staff=True,
                is_superuser=True,
                is_active=True
            )
            
            print(f"✅ Admin user created: {admin_user.username}")
            print(f"✅ Email: {admin_user.email}")
            print(f"✅ Staff: {admin_user.is_staff}")
            print(f"✅ Superuser: {admin_user.is_superuser}")
            print(f"✅ Active: {admin_user.is_active}")
            
            # Verify password
            if admin_user.check_password('admin123'):
                print("✅ Password verification: SUCCESS!")
            else:
                print("❌ Password verification: FAILED!")
            
            print("=== POSTGRESQL ADMIN USER CREATION COMPLETE ===")
            return True
            
    except Exception as e:
        print(f"❌ Error creating admin user: {str(e)}")
        print("=== POSTGRESQL ADMIN USER CREATION FAILED ===")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("🔥 POSTGRESQL ADMIN FIX - ULTIMATE SOLUTION")
    print("This WILL create the admin user in PostgreSQL!")
    print("=" * 50)
    
    success = create_postgresql_admin()
    
    if success:
        print("\n🎉 SUCCESS! Admin user created in PostgreSQL!")
        print("Username: admin")
        print("Password: admin123")
        print("=" * 50)
        sys.exit(0)
    else:
        print("\n💥 FAILED! Admin user creation failed!")
        print("=" * 50)
        sys.exit(1)
