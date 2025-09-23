#!/usr/bin/env python
"""
Create admin using Django management command
"""

import os
import sys
import django
from pathlib import Path

print("🚀 ADMIN MANAGEMENT COMMAND")
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
    
    print("\n2. Running Django management command...")
    from django.core.management import execute_from_command_line
    
    # Run the create_admin management command
    execute_from_command_line(['manage.py', 'create_admin'])
    print("✅ Management command executed")
    
    print("\n3. Verifying admin user...")
    from django.contrib.auth.models import User
    admin_users = User.objects.filter(username='admin')
    if admin_users.exists():
        admin = admin_users.first()
        print(f"✅ Admin user exists: {admin.username}")
        print(f"✅ Staff: {admin.is_staff}")
        print(f"✅ Superuser: {admin.is_superuser}")
        
        # Test password
        if admin.check_password('admin123'):
            print("✅ Password works!")
        else:
            print("❌ Password doesn't work!")
    else:
        print("❌ No admin user found!")
    
    print("\n🎉 ADMIN MANAGEMENT COMMAND COMPLETE!")
    
except Exception as e:
    print(f"\n💥 ERROR: {e}")
    import traceback
    traceback.print_exc()

if __name__ == "__main__":
    print("Admin management command complete!")
