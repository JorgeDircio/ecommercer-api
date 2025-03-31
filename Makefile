.PHONY: up down restart build

APP_CONTAINER=fastapi_app
DB_CONTAINER=pgdb
DB_NAME=payments_app
DB_USER=user

# Ejecutar Alembic dentro del contenedor
migrate:
	docker exec -it $(APP_CONTAINER) alembic upgrade head

makemigration:
	docker exec -it $(APP_CONTAINER) alembic revision --autogenerate -m "Auto migration"

psql:
	docker exec -it $(DB_CONTAINER) psql -U $(DB_USER) -d $(DB_NAME)

# Ver tablas creadas
tables:
	docker exec -it $(DB_CONTAINER) psql -U $(DB_USER) -d $(DB_NAME) -c '\dt'

# Ejecutar shell del contenedor
shell:
	docker exec -it $(APP_CONTAINER) bash

# Reiniciar contenedores
restart:
	docker-compose down && docker-compose up --build

rebuild:
	docker-compose build --no-cache
	docker-compose up

up:
	docker-compose up

down:
	docker-compose down

build:
	docker-compose build