#!/usr/bin/env python
"""
Script to backup media files
This copies all uploaded files to a backup folder
"""

import os
import shutil
from datetime import datetime

def backup_media_files():
    """Backup all media files"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Source and destination paths
    media_source = "media"
    backup_dir = f"media_backup_{timestamp}"
    
    if not os.path.exists(media_source):
        print("❌ Media folder not found!")
        return
    
    # Create backup directory
    os.makedirs(backup_dir, exist_ok=True)
    
    print(f"🔄 Backing up media files to {backup_dir}/")
    
    try:
        # Copy all media files
        shutil.copytree(media_source, backup_dir, dirs_exist_ok=True)
        
        # Count files
        file_count = sum(len(files) for _, _, files in os.walk(backup_dir))
        
        print(f"✅ Backed up {file_count} files")
        print(f"📁 Files saved in {backup_dir}/")
        print("📁 You can now commit these files to GitHub")
        
    except Exception as e:
        print(f"❌ Error backing up media files: {e}")

if __name__ == '__main__':
    backup_media_files()



