#!/usr/bin/env python
"""
Script to backup database data to JSON files
This exports all data from your live database
"""

import os
import sys
import django
import json
from datetime import datetime

# Add the project directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'std_portal.settings')
django.setup()

from django.core import serializers
from django.contrib.auth.models import User
from student_app.models import *

def backup_database():
    """Backup all database data to JSON files"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Create backup directory
    backup_dir = f"backup_{timestamp}"
    os.makedirs(backup_dir, exist_ok=True)
    
    print(f"🔄 Creating backup in {backup_dir}/")
    
    # Backup all models
    models_to_backup = [
        User,
        # Add your other models here
        # Student,
        # Course,
        # etc.
    ]
    
    for model in models_to_backup:
        try:
            # Get all objects from the model
            objects = model.objects.all()
            
            # Serialize to JSON
            data = serializers.serialize("json", objects)
            
            # Save to file
            filename = f"{backup_dir}/{model.__name__.lower()}_backup.json"
            with open(filename, 'w') as f:
                f.write(data)
            
            print(f"✅ Backed up {model.__name__}: {objects.count()} records")
            
        except Exception as e:
            print(f"❌ Error backing up {model.__name__}: {e}")
    
    print(f"\n🎉 Backup complete! Files saved in {backup_dir}/")
    print("📁 You can now commit these files to GitHub")

if __name__ == '__main__':
    backup_database()
