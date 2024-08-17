import os
from celery import Celery
# from celery.decorators import task
# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core')


# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

@app.task
def DeleteDoneTask():
    from todo.models import Tasks
    Tasks.objects.filter(status = True).delete()
    print("deletedd")


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    
    sender.add_periodic_task(600.0, DeleteDoneTask.s(), name='delete complated tasks every 10 minutes')
