#!/usr/bin/env python
"""
Backup admin creation script
This will run if the Django management command fails
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
from django.db import transaction

def create_admin_user():
    print("=== BACKUP ADMIN CREATION STARTED ===")
    
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
            
            print("=== BACKUP ADMIN USER VERIFICATION COMPLETE ===")
            return True
        
        # Create new admin user
        with transaction.atomic():
            admin_user = User.objects.create_user(
                username='admin',
                email='admin@example.com',
                password='admin123',
                is_staff=True,
                is_superuser=True
            )
            
            print(f"✅ Admin user created: {admin_user.username}")
            print(f"✅ Email: {admin_user.email}")
            print(f"✅ Staff: {admin_user.is_staff}")
            print(f"✅ Superuser: {admin_user.is_superuser}")
            
            # Verify password
            if admin_user.check_password('admin123'):
                print("✅ Password verification: SUCCESS!")
            else:
                print("❌ Password verification: FAILED!")
            
            print("=== BACKUP ADMIN USER CREATION COMPLETE ===")
            return True
            
    except Exception as e:
        print(f"❌ Error creating admin user: {str(e)}")
        print("=== BACKUP ADMIN USER CREATION FAILED ===")
        return False

if __name__ == "__main__":
    success = create_admin_user()
    if success:
        print("🎉 Admin user creation successful!")
        sys.exit(0)
    else:
        print("💥 Admin user creation failed!")
        sys.exit(1)


