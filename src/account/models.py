from datetime import date

from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _

from account.validators import validate_min_year

GENDER_CHOICES = [
    ('male', 'мужской'),
    ('female', 'женский'),
]


class User(AbstractUser):
    """Изменение модели User."""
    email = models.EmailField(verbose_name=_('Электронная почта'),
                              help_text=_('Электронная почта'),
                              unique=True)
    biography = models.TextField(
        verbose_name=_('Биография'),
        help_text=_('Биография'), blank=True, null=True
        )
    birthday = models.DateField(
        verbose_name=_('Дата рождения'),
        help_text=_('Дата рождения'),
        blank=True,  null=True,
        validators=[
            MaxValueValidator(
                limit_value=date.today,
                message=_('Дата рожденияне может быть позже сегодняшнего дня')
                ),
            MinValueValidator(
                limit_value=validate_min_year,
                message=_('Дата рождения не может быть больше, '
                          'чем 150 лет назад'))
                ]
        )
    phone = PhoneNumberField(verbose_name=_('Номер телефона'),
                             help_text=_('Номер телефона'),
                             blank=True,  null=True, unique=True)
    gender = models.CharField(
        verbose_name=_('Пол'),
        help_text=_('Пол'),
        choices=GENDER_CHOICES, blank=True,  null=True,
    )

    user_picture = models.ImageField(
        verbose_name=_('Аватарка'),
        help_text=_('Аватарка'),
        upload_to='account/',
        blank=True, null=True,
    )

    class Meta:
        verbose_name = _('Пользователь')
        verbose_name_plural = _('Пользователи')

    def __str__(self) -> str:
        return f'{self.username}'
