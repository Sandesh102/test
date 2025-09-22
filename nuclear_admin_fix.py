#!/usr/bin/env python
"""
NUCLEAR ADMIN FIX - This WILL work!
Direct database manipulation to create admin user
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
from django.db import connection
from django.contrib.auth.hashers import make_password
import sqlite3

def nuclear_admin_fix():
    print("🚀 NUCLEAR ADMIN FIX STARTED")
    print("=" * 50)
    
    try:
        # Method 1: Try Django ORM
        print("Method 1: Django ORM approach...")
        try:
            # Delete existing admin if exists
            User.objects.filter(username='admin').delete()
            print("✅ Deleted existing admin user")
            
            # Create new admin
            admin_user = User.objects.create_user(
                username='admin',
                email='admin@example.com',
                password='admin123',
                is_staff=True,
                is_superuser=True,
                is_active=True
            )
            print(f"✅ Django ORM: Admin created - {admin_user.username}")
            print(f"✅ Django ORM: Staff - {admin_user.is_staff}")
            print(f"✅ Django ORM: Superuser - {admin_user.is_superuser}")
            
            # Verify
            if admin_user.check_password('admin123'):
                print("✅ Django ORM: Password verification SUCCESS!")
                return True
            else:
                print("❌ Django ORM: Password verification FAILED!")
                
        except Exception as e:
            print(f"❌ Django ORM failed: {e}")
        
        # Method 2: Direct SQLite manipulation
        print("\nMethod 2: Direct SQLite approach...")
        try:
            db_path = os.path.join(project_dir, 'db.sqlite3')
            if not os.path.exists(db_path):
                print("❌ Database file not found!")
                return False
            
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            
            # Delete existing admin
            cursor.execute("DELETE FROM auth_user WHERE username = 'admin'")
            print("✅ SQLite: Deleted existing admin")
            
            # Create admin user directly
            hashed_password = make_password('admin123')
            cursor.execute("""
                INSERT INTO auth_user (username, first_name, last_name, email, password, is_staff, is_active, is_superuser, date_joined, last_login)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, datetime('now'), NULL)
            """, ('admin', '', '', 'admin@example.com', hashed_password, 1, 1, 1))
            
            conn.commit()
            print("✅ SQLite: Admin user created directly")
            
            # Verify
            cursor.execute("SELECT id, username, is_staff, is_superuser FROM auth_user WHERE username = 'admin'")
            result = cursor.fetchone()
            if result:
                print(f"✅ SQLite: Admin found - ID: {result[0]}, Username: {result[1]}")
                print(f"✅ SQLite: Staff: {bool(result[2])}, Superuser: {bool(result[3])}")
                conn.close()
                return True
            else:
                print("❌ SQLite: Admin not found after creation!")
                conn.close()
                return False
                
        except Exception as e:
            print(f"❌ SQLite approach failed: {e}")
            if 'conn' in locals():
                conn.close()
        
        # Method 3: Force create with raw SQL
        print("\nMethod 3: Raw SQL approach...")
        try:
            with connection.cursor() as cursor:
                # Delete existing
                cursor.execute("DELETE FROM auth_user WHERE username = 'admin'")
                print("✅ Raw SQL: Deleted existing admin")
                
                # Create with raw SQL
                hashed_password = make_password('admin123')
                cursor.execute("""
                    INSERT INTO auth_user (username, first_name, last_name, email, password, is_staff, is_active, is_superuser, date_joined)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, NOW())
                """, ['admin', '', '', 'admin@example.com', hashed_password, True, True, True])
                
                print("✅ Raw SQL: Admin user created")
                
                # Verify
                cursor.execute("SELECT id, username, is_staff, is_superuser FROM auth_user WHERE username = 'admin'")
                result = cursor.fetchone()
                if result:
                    print(f"✅ Raw SQL: Admin found - ID: {result[0]}, Username: {result[1]}")
                    print(f"✅ Raw SQL: Staff: {result[2]}, Superuser: {result[3]}")
                    return True
                else:
                    print("❌ Raw SQL: Admin not found after creation!")
                    return False
                    
        except Exception as e:
            print(f"❌ Raw SQL approach failed: {e}")
        
        print("\n💥 ALL METHODS FAILED!")
        return False
        
    except Exception as e:
        print(f"💥 NUCLEAR FIX FAILED: {e}")
        return False

if __name__ == "__main__":
    print("🔥 NUCLEAR ADMIN FIX - ULTIMATE SOLUTION")
    print("This WILL create the admin user!")
    print("=" * 50)
    
    success = nuclear_admin_fix()
    
    if success:
        print("\n🎉 SUCCESS! Admin user created!")
        print("Username: admin")
        print("Password: admin123")
        print("=" * 50)
        sys.exit(0)
    else:
        print("\n💥 FAILED! All methods exhausted!")
        print("=" * 50)
        sys.exit(1)
