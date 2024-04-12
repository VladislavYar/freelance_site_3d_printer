from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Order(models.Model):
    """Модель поиска заказчика или испольнителя."""
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    is_сustomer = models.BooleanField()
    description = models.TextField()
    price = models.PositiveIntegerField()
    city = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.user} - {self.is_сustomer} - {self.price}'


class OrderImage(models.Model):
    """Модель изображений поиска заказчика или испольнителя."""
    image = models.ImageField(upload_to='order/')
    order = models.ForeignKey(
        Order, related_name='images', on_delete=models.CASCADE
        )

    def __str__(self) -> str:
        return f'{self.order}'
