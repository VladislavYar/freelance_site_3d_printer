# freelance_site_3d_printer

## Описание
Сайт, посвященный поиску заказчиков и исполнителей работ на 3D-принтере.

## Как запустить проект:

1. В терминале, перейдите в каталог, в который будет загружаться приложение:
```
cd 
```
Клонируйте репозиторий:
```
git clone git@github.com:VladislavYar/freelance_site_3d_printer.git
```
### На данном этапе создайте env-файл по шаблону из раздела выше

2. Cоздать и активировать виртуальное окружение:

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

3. Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

4. Создайте в папке `infra` файл `.env` и заполните его по шаблону [.env.example](https://github.com/VladislavYar/freelance_site_3d_printer/tree/develop/infra/.env.example)

5. Запустите проект комадной:
```
make project-init-dev # Для первого запуска.
make project-start-dev # Для последующих.
```

Теперь проект доступен по адресу http://localhost/

## Cтек проекта
Python v3.11, Django, postgreSQL, Docker
