from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django.forms import ImageField, CharField

from core.widgets import CastomClearableFileInput


User = get_user_model()


class CastomUserCreationForm(UserCreationForm):
    """
    Класс, для переопределения необходимых полей регистрации пользователя.
    """
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')


class CastomUserChangeForm(UserChangeForm):
    """
    Класс, для переопределения необходимых полей изменения данных пользователя.
    """
    user_picture = ImageField(label='Аватарка', required=False,
                                    widget=CastomClearableFileInput)
    username = CharField(label='Логин')
    password = None

    class Meta(UserChangeForm.Meta):
        model = User
        fields = ('username', 'first_name', 'last_name', 'gender', 'birthday',
                  'biography', 'phone', 'user_picture')
