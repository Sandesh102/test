#!/usr/bin/env python
"""
Simple admin creation - guaranteed to work
"""

import os
import sys
import django
from pathlib import Path

print("🚀 SIMPLE ADMIN CREATION")
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
    
    print("\n2. Creating admin user...")
    from django.contrib.auth.models import User
    
    # Delete any existing admin users
    User.objects.filter(username='admin').delete()
    print("✅ Deleted existing admin users")
    
    # Create new admin user
    admin = User.objects.create_superuser(
        username='admin',
        email='admin@test.com',
        password='admin123'
    )
    print(f"✅ Admin user created: {admin.username}")
    
    print("\n3. Testing login...")
    from django.contrib.auth import authenticate
    user = authenticate(username='admin', password='admin123')
    if user:
        print("✅ LOGIN TEST: SUCCESS!")
        print(f"✅ User: {user.username}")
        print(f"✅ Staff: {user.is_staff}")
        print(f"✅ Superuser: {user.is_superuser}")
    else:
        print("❌ LOGIN TEST: FAILED!")
    
    print("\n🎉 ADMIN CREATION COMPLETE!")
    print("✅ Username: admin")
    print("✅ Password: admin123")
    
except Exception as e:
    print(f"\n💥 ERROR: {e}")
    import traceback
    traceback.print_exc()

if __name__ == "__main__":
    print("Simple admin creation complete!")
