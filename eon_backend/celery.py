import os

from celery import Celery

# set the default Django settings module for the 'celery' program.
# always default to local. QA/Production must be explicit
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eon_backend.settings.dev')

app = Celery('eon_backend')

# Using a string here means the worker don't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
