from django.contrib.auth.views import (LoginView, LogoutView,
                                       PasswordChangeDoneView,
                                       PasswordChangeView,
                                       PasswordResetCompleteView,
                                       PasswordResetConfirmView,
                                       PasswordResetDoneView,
                                       PasswordResetView)
from django.urls import path

from account.views import SignUpView, profile, profile_update

app_name = 'account'

urlpatterns = [
        path(
            # Профиль пользователя
            '',
            profile, name='profile'),

        path(
            # Редактирование профиля
            'edit/',
            profile_update, name='edit'),
        path(
            # Регистрация
            'signup/', SignUpView.as_view(), name='signup'),
        path(
            # Авторизация
            'login/',
            LoginView.as_view(template_name='account/login.html'),
            name='login'
        ),
        path(
            # Выход
            'logout/',
            LogoutView.as_view(template_name='account/logged_out.html'),
            name='logout'
        ),
        path(
            # Смена пароля
            'password_change/',
            PasswordChangeView.as_view(
                template_name='account/password_change_form.html'),
            name='password_change_form'
        ),
        path(
            # Сообщение об успешном изменении пароля
            'password_change/done/',
            PasswordChangeDoneView.as_view(
                template_name='account/password_change_done.html'),
            name='password_change_done'
        ),
        path(
            # Восстановление пароля
            'password_reset/',
            PasswordResetView.as_view(
                template_name='account/password_reset_form.html'),
            name='password_reset_form'
        ),
        path(
            # Сообщение об отправке ссылки для восстановления пароля
            'password_reset/done/',
            PasswordResetDoneView.as_view(
                template_name='account/password_reset_done.html'),
            name='password_reset_done'
        ),
        path(
            # Вход по ссылке для восстановления пароля
            'reset/<uidb64>/<token>/',
            PasswordResetConfirmView.as_view(
                template_name='account/password_reset_confirm.html'),
            name='password_reset_confirm'
        ),
        path(
            # Сообщение об успешном восстановлении пароля
            'reset/done/',
            PasswordResetCompleteView.as_view(
                template_name='account/password_reset_complete.html'),
            name='password_reset_complete'
        ),
]
