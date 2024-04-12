from django.db import models


class Order(models.Model):
    """Модель поиска заказчика или испольнителя."""
    user = models.ForeignKey('core.User', on_delete=models.PROTECT)
    is_сustomer = models.BooleanField()
    description = models.TextField(blank=True, null=True)
    price = models.PositiveIntegerField()
