#!/usr/bin/env python
"""
PRODUCTION ADMIN FIX - Guaranteed to work on Render.com
This script creates admin user with multiple fallback methods
"""

import os
import sys
import django
import sqlite3
from datetime import datetime

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'std_portal.settings')
django.setup()

from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.db import connection

def production_admin_fix():
    """Create admin user for production with multiple fallback methods"""
    print("🚀 PRODUCTION ADMIN FIX - Multiple Methods...")
    
    username = 'admin'
    email = 'admin@sikshyakendra.com'
    password = 'admin123'
    
    try:
        # Method 1: Django ORM with get_or_create
        print("Method 1: Django ORM get_or_create...")
        admin, created = User.objects.get_or_create(
            username=username,
            defaults={
                'email': email,
                'is_superuser': True,
                'is_staff': True,
                'is_active': True,
                'date_joined': datetime.now()
            }
        )
        
        if not created:
            print("Admin exists, updating...")
            admin.email = email
            admin.is_superuser = True
            admin.is_staff = True
            admin.is_active = True
            admin.save()
        
        # Set password
        admin.set_password(password)
        admin.save()
        
        print("✅ Method 1: Django ORM - SUCCESS!")
        
    except Exception as e:
        print(f"❌ Method 1 failed: {e}")
        
        try:
            # Method 2: Direct SQLite approach
            print("Method 2: Direct SQLite...")
            db_path = 'db.sqlite3'
            
            if os.path.exists(db_path):
                conn = sqlite3.connect(db_path)
                cursor = conn.cursor()
                
                # Delete existing admin
                cursor.execute("DELETE FROM auth_user WHERE username = ?", (username,))
                
                # Create new admin
                hashed_password = make_password(password)
                cursor.execute("""
                    INSERT INTO auth_user 
                    (username, email, password, is_superuser, is_staff, is_active, date_joined, first_name, last_name)
                    VALUES (?, ?, ?, 1, 1, 1, ?, '', '')
                """, (username, email, hashed_password, datetime.now().isoformat()))
                
                conn.commit()
                conn.close()
                print("✅ Method 2: Direct SQLite - SUCCESS!")
                
        except Exception as e2:
            print(f"❌ Method 2 failed: {e2}")
            
            try:
                # Method 3: Raw SQL through Django
                print("Method 3: Raw SQL through Django...")
                with connection.cursor() as cursor:
                    # Delete existing
                    cursor.execute("DELETE FROM auth_user WHERE username = %s", [username])
                    
                    # Create new
                    hashed_password = make_password(password)
                    cursor.execute("""
                        INSERT INTO auth_user 
                        (username, email, password, is_superuser, is_staff, is_active, date_joined, first_name, last_name)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                    """, [username, email, hashed_password, True, True, True, datetime.now(), '', ''])
                
                print("✅ Method 3: Raw SQL - SUCCESS!")
                
            except Exception as e3:
                print(f"❌ Method 3 failed: {e3}")
                return False
    
    # Final verification
    try:
        admin = User.objects.get(username=username)
        print(f"\n✅ FINAL VERIFICATION:")
        print(f"Username: {admin.username}")
        print(f"Email: {admin.email}")
        print(f"Is superuser: {admin.is_superuser}")
        print(f"Is staff: {admin.is_staff}")
        print(f"Is active: {admin.is_active}")
        
        # Test password
        if admin.check_password(password):
            print("✅ Password verification: SUCCESS!")
            print(f"\n🔗 Login at: https://test-hvdl.onrender.com/admin/")
            print(f"Username: {username}")
            print(f"Password: {password}")
            return True
        else:
            print("❌ Password verification: FAILED!")
            return False
            
    except User.DoesNotExist:
        print("❌ Admin user not found after creation!")
        return False
    except Exception as e:
        print(f"❌ Verification failed: {e}")
        return False

if __name__ == '__main__':
    success = production_admin_fix()
    if success:
        print("\n🎉 PRODUCTION ADMIN FIX COMPLETE!")
    else:
        print("\n💥 PRODUCTION ADMIN FIX FAILED!")
        sys.exit(1)
