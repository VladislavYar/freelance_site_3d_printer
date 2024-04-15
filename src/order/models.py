from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from order.constants import PRICE_MAX, PRICE_MIN


User = get_user_model()


class Order(models.Model):
    """Модель поиска заказчика или испольнителя."""
    user = models.ForeignKey(
        User, on_delete=models.PROTECT,
        verbose_name=_('Заказчик/исполнитель'),
        help_text=_('Заказчик/исполнитель')
        )
    is_customer = models.BooleanField(
        verbose_name=_('Заказчик'), help_text=_('Заказчик')
        )
    description = models.TextField(
        verbose_name=_('Описание'), help_text=_('Описание')
        )
    price = models.PositiveIntegerField(
        verbose_name=_('Оплата'), help_text=_('Оплата'),
        validators=(
            MinValueValidator(PRICE_MIN), MaxValueValidator(PRICE_MAX),
            )
        )
    city = models.CharField(
        max_length=50, verbose_name=_('Город выполения'),
        help_text=_('Город выполения')
        )
    date = models.DateField(
        auto_now_add=True, verbose_name=_('Дата создания'),
        help_text=_('Дата создания')
        )

    class Meta:
        ordering = ('-id', '-date',)
        verbose_name = _('Заказ/предложение')
        verbose_name_plural = _('Заказы/предложения')

    def __str__(self) -> str:
        return f'{self.user} - {self.is_customer} - {self.price}'


class OrderImage(models.Model):
    """Модель изображений поиска заказчика или испольнителя."""
    image = models.ImageField(
        upload_to='order/', verbose_name=_('Изображение заказа/предложения'),
        help_text=_('Изображение заказа/предложения')
        )
    order = models.ForeignKey(
        Order, related_name='images', on_delete=models.CASCADE,
        verbose_name=_('Заказ/предложение'),
        help_text=_('Заказа/предложение')
        )

    class Meta:
        verbose_name = _('Изображение заказа/предложения')
        verbose_name_plural = _('Изображении заказов/предложений')

    def __str__(self) -> str:
        return f'{self.order}'
