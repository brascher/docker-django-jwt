#!/bin/sh

MYSQL_HOST="mysql"

until nc -z -v -w60 $MYSQL_HOST 3306
do
  echo "Waiting for db connection ..."
  sleep 5
done 
python manage.py makemigrations
python manage.py migrate

exec "$@"
