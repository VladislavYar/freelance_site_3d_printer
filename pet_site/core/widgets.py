from django.forms import ClearableFileInput


class CastomClearableFileInput(ClearableFileInput):
    """Кастомный виджет формы файла."""
    template_name = 'forms/widgets/clearable_file_input.html'
