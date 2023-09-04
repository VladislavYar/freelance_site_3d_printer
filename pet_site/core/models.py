from datetime import date

from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from core.validators import validate_min_year

GENDER_CHOICES = [
    ('male', 'мужской'),
    ('female', 'женский'),
]


class User(AbstractUser):
    """Изменение модели User."""
    email = models.EmailField(verbose_name='Электронная почта',
                              help_text='Электронная почта',
                              unique=True, blank=False, null=False, )
    biography = models.TextField('биография', blank=True, null=True)
    birthday = models.DateField(
        verbose_name='Дата рождения',
        help_text='Дата рождения',
        blank=True,  null=True,
        validators=[
            MaxValueValidator(
                limit_value=date.today,
                message='дата рожденияне может быть позже сегодняшнего дня'),
            MinValueValidator(
                limit_value=validate_min_year,
                message='дата рождения не может быть больше, '
                        'чем 150 лет назад')
                ]
        )
    phone = PhoneNumberField(verbose_name='Номер телефона',
                             help_text='Номер телефона',
                             blank=True,  null=True, unique=True)
    gender = models.CharField(
        verbose_name='Пол',
        help_text='Пол',
        choices=GENDER_CHOICES, blank=True,  null=True,
    )

    user_picture = models.ImageField(
        verbose_name='Аватарка',
        help_text='Аватарка',
        upload_to='account/',
        blank=True, null=True,
    )

    def __str__(self) -> str:
        return f'{self.username}'
