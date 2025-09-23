#!/usr/bin/env python
"""
Backup admin creation using Django shell
"""

import os
import sys
import django
from pathlib import Path

print("🚀 BACKUP ADMIN CREATION")
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
    
    print("\n2. Backup admin creation...")
    from django.contrib.auth.models import User
    
    # Delete existing
    User.objects.filter(username='admin').delete()
    print("✅ Deleted existing admin")
    
    # Create new
    admin = User.objects.create_superuser(
        username='admin',
        email='admin@test.com',
        password='admin123'
    )
    print(f"✅ Backup admin created: {admin.username}")
    
    # Verify
    admin = User.objects.get(username='admin')
    print(f"✅ Username: {admin.username}")
    print(f"✅ Staff: {admin.is_staff}")
    print(f"✅ Superuser: {admin.is_superuser}")
    print(f"✅ Active: {admin.is_active}")
    
    if admin.check_password('admin123'):
        print("✅ Password works!")
    else:
        print("❌ Password doesn't work!")
        admin.set_password('admin123')
        admin.save()
        print("✅ Password reset!")
    
    print("\n🎉 BACKUP ADMIN CREATION COMPLETE!")
    
except Exception as e:
    print(f"\n💥 BACKUP ERROR: {e}")
    import traceback
    traceback.print_exc()

if __name__ == "__main__":
    print("Backup admin creation complete!")
