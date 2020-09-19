#!/bin/sh

echo "[INFO] Carregando dados iniciais do sistema..."

echo "[INFO] Carregando dados iniciais para usuários..."
docker-compose exec web python manage.py loaddata users

echo "[INFO] Carregando dados iniciais para ações..."
docker-compose exec web python manage.py loaddata actions