"""
WSGI config for std_portal project.

PostgreSQL Production Configuration
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'std_portal.production')

application = get_wsgi_application()