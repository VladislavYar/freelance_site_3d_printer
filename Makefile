# Команды для dev
clear-volumes-dev: # Удаление Volumes
	docker compose -f ./infra/docker-compose.dev.yml --env-file ./infra/.env down --volumes

start-containers-dev: # Запуск контейнеров
	docker compose -f ./infra/docker-compose.dev.yml --env-file ./infra/.env up -d;
	@sleep 3;

start-server-dev: # Запуск сервера
	python src/manage.py runserver

add-db-locality-dev: # Добавление населённых пунктов в БД
	python src/manage.py locality_in_db

migrate-dev: # Выполнить миграции Django
	python src/manage.py migrate

createsuperuser-dev: # Создать супер пользователя
	python src/manage.py createsuperuser --noinput

project-init-dev: # Инициализировать проект
	make clear-volumes-dev start-containers-dev migrate-dev createsuperuser-dev add-db-locality-dev start-server-dev

project-start-dev: # Запустить проект
	make start-containers-dev start-server-dev

containers-stop-dev: # Остановить контейнеры
	docker compose -f ./infra/docker-compose.dev.yml  --env-file .env down;

celery-worker-start: # Запуск worker
	cd src/ && celery -A freelance_site worker -l info --without-gossip --without-mingle --without-heartbeat -Ofair --pool=solo

celery-beat-start: # Запуск beat
	cd src/ && celery -A freelance_site beat --loglevel=INFO