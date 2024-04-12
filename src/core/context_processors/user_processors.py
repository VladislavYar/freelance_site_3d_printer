from typing import Union

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm
from django.core.handlers.wsgi import WSGIRequest
from django.db.models.fields.files import ImageFieldFile
from django.shortcuts import get_object_or_404

User = get_user_model()


def login_form(request: WSGIRequest) -> dict[AuthenticationForm]:
    """Добавляет форму входа."""
    return {
        'login_form': AuthenticationForm()
    }


def reset_form(request: WSGIRequest) -> dict[PasswordResetForm]:
    """Добавляет форму востановления пароля."""
    return {
        'reset_form': PasswordResetForm()
    }


def get_user_picture(request:
                     WSGIRequest) -> Union[dict[ImageFieldFile], None]:
    """Добавляет аватар пользователя."""
    user_picture = None
    if request.user.is_authenticated:
        user = get_object_or_404(User, username=request.user)
        user_picture = user.user_picture
    return {
        'user_picture': user_picture
    }
