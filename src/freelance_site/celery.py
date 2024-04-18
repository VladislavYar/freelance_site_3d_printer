import os

from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'freelance_site.settings')
app = Celery('freelance_site')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'del_orders_more_30_days': {
        'task': 'order.tasks.del_orders_more_30_days',
        'schedule': crontab(hour=23),
    }
}
