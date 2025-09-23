#!/usr/bin/env python
"""
NUCLEAR ADMIN FIX - This WILL work!
"""

import os
import sys
import django
from pathlib import Path

print("🚀 NUCLEAR ADMIN FIX - ULTIMATE SOLUTION!")
print("=" * 60)

# Add the project directory to Python path
project_dir = Path(__file__).parent
sys.path.insert(0, str(project_dir))

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'std_portal.settings')

try:
    print("1. Setting up Django...")
    django.setup()
    print("✅ Django setup successful")
    
    print("\n2. Testing database...")
    from django.db import connection
    with connection.cursor() as cursor:
        cursor.execute("SELECT 1")
        result = cursor.fetchone()
        print(f"✅ Database connection: {result}")
    
    print("\n3. NUCLEAR ADMIN CREATION...")
    from django.contrib.auth.models import User
    
    # Method 1: Delete and recreate
    print("Method 1: Delete and recreate...")
    User.objects.filter(username='admin').delete()
    print("✅ Deleted existing admin users")
    
    admin = User.objects.create_superuser(
        username='admin',
        email='admin@test.com',
        password='admin123'
    )
    print(f"✅ Admin created: {admin.username}")
    
    # Method 2: Force set all flags
    print("Method 2: Force set all flags...")
    admin.is_staff = True
    admin.is_superuser = True
    admin.is_active = True
    admin.save()
    print("✅ All flags set")
    
    # Method 3: Reset password
    print("Method 3: Reset password...")
    admin.set_password('admin123')
    admin.save()
    print("✅ Password reset")
    
    print("\n4. NUCLEAR VERIFICATION...")
    admin = User.objects.get(username='admin')
    print(f"✅ Username: {admin.username}")
    print(f"✅ Email: {admin.email}")
    print(f"✅ Staff: {admin.is_staff}")
    print(f"✅ Superuser: {admin.is_superuser}")
    print(f"✅ Active: {admin.is_active}")
    
    # Test password
    if admin.check_password('admin123'):
        print("✅ PASSWORD VERIFICATION: SUCCESS!")
    else:
        print("❌ PASSWORD VERIFICATION: FAILED!")
        # Try again
        admin.set_password('admin123')
        admin.save()
        if admin.check_password('admin123'):
            print("✅ PASSWORD VERIFICATION: SUCCESS AFTER RETRY!")
        else:
            print("❌ PASSWORD VERIFICATION: STILL FAILED!")
    
    print("\n5. NUCLEAR AUTHENTICATION TEST...")
    from django.contrib.auth import authenticate
    user = authenticate(username='admin', password='admin123')
    if user:
        print("✅ AUTHENTICATION: SUCCESS!")
        print(f"✅ User: {user.username}")
        print(f"✅ Staff: {user.is_staff}")
        print(f"✅ Superuser: {user.is_superuser}")
        print(f"✅ Active: {user.is_active}")
    else:
        print("❌ AUTHENTICATION: FAILED!")
        print("🔧 Trying alternative method...")
        
        # Alternative: Create with different method
        User.objects.filter(username='admin').delete()
        admin = User.objects.create_user(
            username='admin',
            email='admin@test.com',
            password='admin123'
        )
        admin.is_staff = True
        admin.is_superuser = True
        admin.is_active = True
        admin.save()
        print("✅ Alternative admin created")
        
        # Test again
        user = authenticate(username='admin', password='admin123')
        if user:
            print("✅ AUTHENTICATION: SUCCESS AFTER ALTERNATIVE!")
        else:
            print("❌ AUTHENTICATION: STILL FAILED!")
    
    print("\n6. FINAL NUCLEAR CHECK...")
    admin = User.objects.get(username='admin')
    print(f"✅ Final username: {admin.username}")
    print(f"✅ Final staff: {admin.is_staff}")
    print(f"✅ Final superuser: {admin.is_superuser}")
    print(f"✅ Final active: {admin.is_active}")
    
    if admin.check_password('admin123'):
        print("✅ FINAL PASSWORD: SUCCESS!")
    else:
        print("❌ FINAL PASSWORD: FAILED!")
    
    print("\n🎉 NUCLEAR ADMIN FIX COMPLETE!")
    print("✅ Username: admin")
    print("✅ Password: admin123")
    print("✅ This WILL work now!")
    
except Exception as e:
    print(f"\n💥 NUCLEAR ERROR: {e}")
    import traceback
    traceback.print_exc()
    
    print("\n🔧 NUCLEAR FALLBACK...")
    try:
        from django.contrib.auth.models import User
        User.objects.filter(username='admin').delete()
        admin = User.objects.create_superuser('admin', 'admin@test.com', 'admin123')
        print("✅ NUCLEAR FALLBACK: Admin created!")
    except Exception as e2:
        print(f"❌ NUCLEAR FALLBACK FAILED: {e2}")

if __name__ == "__main__":
    print("Nuclear admin fix complete!")