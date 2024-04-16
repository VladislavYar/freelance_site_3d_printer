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

    def get_delete_images_id(self):
        """Возвращает ключи для удаления."""
        regex_delete_image = re.compile(r'^delete_image_\d+$')
        regex_id = re.compile(r'\d+')
        return [
            int(
                re.search(regex_id, delete_image).group(0)
                ) for delete_image in filter(
                regex_delete_image.match, self.data.keys()
                )
            ]

    def clean_images(self):
        """Валидация сохранения изображений."""
        images = self.cleaned_data.get('images')
        delete_id = self.get_delete_images_id()
        count_order_images = 0
        count_delete_id = len(delete_id)
        if self.instance.id:
            order_images = self.instance.images.all()
            count_order_images = order_images.count()
            if count_delete_id != self.instance.images.filter(
                id__in=delete_id
                 ).count():
                raise ValidationError(
                    _('Не верные индексы изображений для удаления.')
                    )
        count_image = count_order_images - count_delete_id + len(images)
        if count_image > FILES_MAX:
            raise ValidationError(
                _('Изображений должно быть не больше '
                  f'{FILES_MAX}.')
                )
        return images
