#!/usr/bin/env python
"""
Script to create a superuser account for the student portal
Run this script to create an admin account
"""

import os
import sys
import django

# Add the project directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'std_portal.settings')
django.setup()

from django.contrib.auth.models import User

def create_superuser():
    """Create a superuser account"""
    username = 'admin'
    email = 'admin@sikshyakendra.com'
    password = 'admin123'
    
    # Check if superuser already exists
    if User.objects.filter(username=username).exists():
        print(f"Superuser '{username}' already exists!")
        return
    
    # Create superuser
    User.objects.create_superuser(
        username=username,
        email=email,
        password=password
    )
    
    print("✅ Superuser created successfully!")
    print(f"Username: {username}")
    print(f"Email: {email}")
    print(f"Password: {password}")
    print("\n🔗 You can now login at: https://test-hvdl.onrender.com/admin/")

if __name__ == '__main__':
    create_superuser()

