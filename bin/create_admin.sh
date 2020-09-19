#!/bin/sh

echo "[INFO] Criando um administrador para o sistema..."

docker-compose exec web python manage.py createsuperuser