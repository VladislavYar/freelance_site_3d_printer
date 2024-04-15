from django import forms

from order.constants import FILES_MAX


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleImageField(forms.ImageField):
    """Поле множественного выбора изображений."""
    def __init__(self, *args, **kwargs):
        kwargs.setdefault(
            "widget", MultipleFileInput(
                attrs={
                    'class': 'form-control',
                    'max-files': FILES_MAX,
                    }
                )
            )
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_image_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_image_clean(d, initial) for d in data]
        else:
            result = single_image_clean(data, initial)
        return result
