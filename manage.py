#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'std_portal.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    
    # Create superuser if it doesn't exist
    try:
        from django.contrib.auth.models import User
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username='admin',
                email='admin@sikshyakendra.com',
                password='admin123'
            )
            print("✅ Superuser 'admin' created successfully!")
        else:
            print("ℹ️  Superuser 'admin' already exists!")
    except Exception as e:
        print(f"⚠️  Could not create superuser: {e}")
    
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()