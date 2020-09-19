#!/bin/sh

echo "[INFO] Iniciando os testes do sistema..."

docker-compose exec web python manage.py test