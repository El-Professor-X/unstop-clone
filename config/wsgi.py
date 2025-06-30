# config/wsgi.py
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_wsgi_application()

# --- Temporary auto-migration + superuser creation ---
from django.core.management import call_command
from django.contrib.auth import get_user_model

try:
    call_command('migrate')
    call_command('collectstatic', interactive=False)
    
    User = get_user_model()
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'adminpass123')
        print("✅ Superuser created.")
    else:
        print("⚠️ Superuser already exists.")
except Exception as e:
    print("⚠️ Error during migration/superuser:", e)
