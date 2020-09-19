#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "[INFO] Iniciando postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "[INFO] PostgreSQL Iniciado"
fi

echo "[INFO] Rodando as migrações"

python manage.py flush --no-input
python manage.py migrate

echo "[INFO] Rodando os testes"

python manage.py test

exec "$@"