#!/usr/bin/env python
"""
Complete backup script for your student portal
This backs up both database data and media files
"""

import os
import sys
import django
import json
import shutil
from datetime import datetime

# Add the project directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'std_portal.settings')
django.setup()

from django.core import serializers
from django.contrib.auth.models import User

def complete_backup():
    """Complete backup of database and media files"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_dir = f"complete_backup_{timestamp}"
    
    print(f"🚀 Starting complete backup...")
    print(f"📁 Backup directory: {backup_dir}/")
    
    # Create backup directory
    os.makedirs(backup_dir, exist_ok=True)
    
    # 1. Backup database
    print("\n🔄 Backing up database...")
    try:
        # Backup users
        users = User.objects.all()
        user_data = serializers.serialize("json", users)
        
        with open(f"{backup_dir}/users_backup.json", 'w') as f:
            f.write(user_data)
        
        print(f"✅ Users backed up: {users.count()} records")
        
        # Add more models here as needed
        # students = Student.objects.all()
        # courses = Course.objects.all()
        # etc.
        
    except Exception as e:
        print(f"❌ Database backup error: {e}")
    
    # 2. Backup media files
    print("\n🔄 Backing up media files...")
    try:
        if os.path.exists("media"):
            shutil.copytree("media", f"{backup_dir}/media", dirs_exist_ok=True)
            
            # Count files
            file_count = sum(len(files) for _, _, files in os.walk(f"{backup_dir}/media"))
            print(f"✅ Media files backed up: {file_count} files")
        else:
            print("⚠️  No media folder found")
            
    except Exception as e:
        print(f"❌ Media backup error: {e}")
    
    # 3. Create backup info file
    backup_info = {
        "timestamp": timestamp,
        "backup_date": datetime.now().isoformat(),
        "description": "Complete backup of student portal data",
        "files_included": [
            "users_backup.json",
            "media/ (all uploaded files)"
        ]
    }
    
    with open(f"{backup_dir}/backup_info.json", 'w') as f:
        json.dump(backup_info, f, indent=2)
    
    print(f"\n🎉 Complete backup finished!")
    print(f"📁 All files saved in: {backup_dir}/")
    print(f"📁 You can now commit this folder to GitHub")
    print(f"\n📋 To restore data:")
    print(f"   1. Copy files from {backup_dir}/ to your project")
    print(f"   2. Run: python manage.py loaddata users_backup.json")
    print(f"   3. Copy media files to media/ folder")

if __name__ == '__main__':
    complete_backup()



