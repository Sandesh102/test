#!/usr/bin/env python
"""
Deploy Admin Fix to Production
This script helps you deploy the admin fix to production
"""

import subprocess
import sys
import os

def deploy_admin_fix():
    """Deploy the admin fix to production"""
    print("🚀 DEPLOYING ADMIN FIX TO PRODUCTION...")
    
    try:
        # Check if git is available
        result = subprocess.run(['git', '--version'], capture_output=True, text=True)
        if result.returncode != 0:
            print("❌ Git not found. Please install Git first.")
            return False
        
        # Add all files
        print("📁 Adding files to git...")
        subprocess.run(['git', 'add', '.'], check=True)
        
        # Commit changes
        print("💾 Committing changes...")
        subprocess.run(['git', 'commit', '-m', 'Fix admin login issue - production admin fix'], check=True)
        
        # Push to production
        print("🚀 Pushing to production...")
        subprocess.run(['git', 'push', 'origin', 'main'], check=True)
        
        print("✅ DEPLOYMENT INITIATED!")
        print("⏳ Please wait 2-3 minutes for Render to build and deploy...")
        print("🔗 Check your deployment at: https://dashboard.render.com")
        print("🔗 Test admin login at: https://test-hvdl.onrender.com/admin/")
        print("   Username: admin")
        print("   Password: admin123")
        
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Git command failed: {e}")
        return False
    except Exception as e:
        print(f"❌ Deployment failed: {e}")
        return False

if __name__ == '__main__':
    success = deploy_admin_fix()
    if success:
        print("\n🎉 DEPLOYMENT COMPLETE!")
    else:
        print("\n💥 DEPLOYMENT FAILED!")
        sys.exit(1)
