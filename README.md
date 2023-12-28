# freelance_site_3d_printer

## Описание
Сайт, посвященный поиску заказчиков и исполнителей работ на 3D-принтере.

## Шаблон наполнения env-файла
- DB_ENGINE=django.db.backends.postgresql # указываем, что работаем с postgresql
- DB_NAME=postgres # имя базы данных
- POSTGRES_USER=postgres # логин для подключения к базе данных
- POSTGRES_PASSWORD=postgres # пароль для подключения к БД
- DB_HOST=localhost # адресс БД
- DB_PORT=5432 # порт для подключения к БД
- SECRET_KEY=django-insecure-********************** # секретный ключ

## Как запустить проект:

В терминале, перейдите в каталог, в который будет загружаться приложение:
```
cd 
```
Клонируйте репозиторий:
```
git clone git@github.com:VladislavYar/freelance_site_3d_printer.git
```
### На данном этапе создайте env-файл по шаблону из раздела выше

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выпоните миграции:
```
python manage.py makemigrations
python manage.py migrate
```

Создайте суперюзера (логин\почта\пароль):
```
python manage.py createsuperuser
```
Соберите статические файлы:
```
python manage.py collectstatic --no-input
```
Запуск проект:
```
python manage.py runserver
```
Теперь проект доступен по адресу http://localhost/

## Cтек проекта
Python v3.11, Django, postgreSQL
