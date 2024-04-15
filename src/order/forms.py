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

    def clean_images(self):
        images = self.cleaned_data.get('images')
        if len(images) > FILES_MAX:
            raise ValidationError(
                _(f'Изображений должно быть не боль {FILES_MAX}.')
                )
        return images
