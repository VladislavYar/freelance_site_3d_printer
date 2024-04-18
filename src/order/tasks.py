from datetime import timedelta

from django.utils import timezone

from freelance_site.celery import app
from order.models import Order


@app.task
def del_orders_more_30_days():
    """Удаляет записи старше 30 дней."""
    Order.objects.filter(
        date__lte=timezone.localdate() - timedelta(days=30)
        ).delete()
