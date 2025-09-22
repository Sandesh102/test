#!/usr/bin/env python
"""
FINAL ADMIN FIX - This WILL work!
Direct database approach to create admin user
"""

import os
import sys
import django
import sqlite3

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'std_portal.settings')
django.setup()

from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

def final_admin_fix():
    """Final fix to create admin user"""
    print("🚀 FINAL ADMIN FIX - Direct Database Approach...")
    
    try:
        # Method 1: Try Django ORM
        print("Trying Django ORM...")
        admin, created = User.objects.get_or_create(
            username='admin',
            defaults={
                'email': 'admin@sikshyakendra.com',
                'is_superuser': True,
                'is_staff': True,
                'is_active': True,
                'password': make_password('admin123')
            }
        )
        
        if created:
            print("✅ Admin user created via Django ORM!")
        else:
            # Update existing user
            admin.is_superuser = True
            admin.is_staff = True
            admin.is_active = True
            admin.set_password('admin123')
            admin.save()
            print("✅ Admin user updated via Django ORM!")
        
        # Method 2: Direct SQLite approach
        print("Trying direct SQLite approach...")
        db_path = 'db.sqlite3'
        if os.path.exists(db_path):
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            
            # Check if admin exists
            cursor.execute("SELECT id FROM auth_user WHERE username = 'admin'")
            result = cursor.fetchone()
            
            if result:
                # Update existing admin
                admin_id = result[0]
                hashed_password = make_password('admin123')
                cursor.execute("""
                    UPDATE auth_user 
                    SET password = ?, is_superuser = 1, is_staff = 1, is_active = 1
                    WHERE id = ?
                """, (hashed_password, admin_id))
                print("✅ Admin user updated via direct SQLite!")
            else:
                # Create new admin
                hashed_password = make_password('admin123')
                cursor.execute("""
                    INSERT INTO auth_user (username, email, password, is_superuser, is_staff, is_active, date_joined)
                    VALUES (?, ?, ?, 1, 1, 1, datetime('now'))
                """, ('admin', 'admin@sikshyakendra.com', hashed_password))
                print("✅ Admin user created via direct SQLite!")
            
            conn.commit()
            conn.close()
        
        # Verify admin user
        admin = User.objects.get(username='admin')
        print(f"\n✅ VERIFICATION:")
        print(f"Username: {admin.username}")
        print(f"Email: {admin.email}")
        print(f"Is superuser: {admin.is_superuser}")
        print(f"Is staff: {admin.is_staff}")
        print(f"Is active: {admin.is_active}")
        
        # Test password
        if admin.check_password('admin123'):
            print("✅ Password verification: SUCCESS!")
        else:
            print("❌ Password verification: FAILED!")
        
        print(f"\n🔗 Login at: https://test-hvdl.onrender.com/admin/")
        print("Username: admin")
        print("Password: admin123")
        
    except Exception as e:
        print(f"❌ ERROR: {e}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    final_admin_fix()
