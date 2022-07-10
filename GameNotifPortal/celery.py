import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GameNotifPortal.settings')

app = Celery('GameNotifPortal')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'send_mail_every_monday_8am': {
        'task': 'usersaccounts.tasks.send_newsletter_every_week',
        'schedule': crontab(minute="*/1"),
    },
}
app.autodiscover_tasks()
