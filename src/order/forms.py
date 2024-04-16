import re

from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from order.constants import PRICE_MAX, FILES_MAX
from order.models import Order, OrderImage
from order.fields import MultipleImageField


class OrderForm(forms.ModelForm):
    """Форма заказа/предложения."""
    images = MultipleImageField(
        required=False,
        label=OrderImage._meta.get_field('image').verbose_name
        )

    class Meta:
        model = Order
        fields = (
            'is_customer',
            'description',
            'price',
            'city',
            'images',
            )
        widgets = {
            'city': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': _('Укажите город'),
                    }
                ),
            'price': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': _('Укажите оплату'),
                    'maxlength': len(str(PRICE_MAX)),
                    }
                ),
            'is_customer': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input',
                    }
                ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': _('Введите описание'),
                    }
                ),
        }

    def get_delete_images_key(self):
        """Возвращает ключи для удаления."""
        regex = re.compile(r'^delete_image_[0-4]{1}$')
        return [
            int(delete_image[-1]) for delete_image in filter(
                regex.match, self.cleaned_data.keys()
                )
            ]

    def clean_images(self):
        """Валидация сохранения изображений."""
        images = self.cleaned_data.get('images')
        count_delete_keys = len(self.get_delete_images_key())
        count_order_images = 0
        if self.instance.id:
            count_order_images = self.instance.images.count()
        count_image = count_order_images - count_delete_keys + len(images)
        if count_image > FILES_MAX:
            raise ValidationError(
                _('Изображений должно быть не больше '
                  f'{FILES_MAX - count_delete_keys}.')
                )
        return images
