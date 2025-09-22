from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.db import transaction
import os

class Command(BaseCommand):
    help = 'Create admin user for deployment'

    def handle(self, *args, **options):
        self.stdout.write("=== ADMIN USER CREATION STARTED ===")
        
        try:
            # Check if admin user already exists
            if User.objects.filter(username='admin').exists():
                admin_user = User.objects.get(username='admin')
                self.stdout.write(f"Admin user already exists: {admin_user.username}")
                
                # Verify password
                if admin_user.check_password('admin123'):
                    self.stdout.write("✅ Password verification: SUCCESS!")
                else:
                    self.stdout.write("⚠️ Password verification: FAILED - Resetting password")
                    admin_user.set_password('admin123')
                    admin_user.save()
                    self.stdout.write("✅ Password reset: SUCCESS!")
                
                # Ensure user is staff and superuser
                if not admin_user.is_staff:
                    admin_user.is_staff = True
                    admin_user.save()
                    self.stdout.write("✅ Staff status: ENABLED")
                
                if not admin_user.is_superuser:
                    admin_user.is_superuser = True
                    admin_user.save()
                    self.stdout.write("✅ Superuser status: ENABLED")
                
                self.stdout.write("=== ADMIN USER VERIFICATION COMPLETE ===")
                return
            
            # Create new admin user
            with transaction.atomic():
                admin_user = User.objects.create_user(
                    username='admin',
                    email='admin@example.com',
                    password='admin123',
                    is_staff=True,
                    is_superuser=True
                )
                
                self.stdout.write(f"✅ Admin user created: {admin_user.username}")
                self.stdout.write(f"✅ Email: {admin_user.email}")
                self.stdout.write(f"✅ Staff: {admin_user.is_staff}")
                self.stdout.write(f"✅ Superuser: {admin_user.is_superuser}")
                
                # Verify password
                if admin_user.check_password('admin123'):
                    self.stdout.write("✅ Password verification: SUCCESS!")
                else:
                    self.stdout.write("❌ Password verification: FAILED!")
                
                self.stdout.write("=== ADMIN USER CREATION COMPLETE ===")
                
        except Exception as e:
            self.stdout.write(f"❌ Error creating admin user: {str(e)}")
            self.stdout.write("=== ADMIN USER CREATION FAILED ===")
            raise