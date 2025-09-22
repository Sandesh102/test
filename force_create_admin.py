#!/usr/bin/env python
"""
Force create admin user - This WILL work!
"""

import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'std_portal.settings')
django.setup()

from django.contrib.auth.models import User

def force_create_admin():
    """Force create admin user"""
    print("🚀 FORCE CREATING ADMIN USER...")
    
    # Delete existing admin if exists
    User.objects.filter(username='admin').delete()
    print("🗑️  Deleted existing admin user")
    
    # Create new admin
    admin = User.objects.create_superuser(
        username='admin',
        email='admin@sikshyakendra.com',
        password='admin123'
    )
    
    print("✅ ADMIN USER CREATED!")
    print("Username: admin")
    print("Password: admin123")
    print("Email: admin@sikshyakendra.com")
    print("🔗 Login at: https://test-hvdl.onrender.com/admin/")
    
    return admin

if __name__ == '__main__':
    force_create_admin()


