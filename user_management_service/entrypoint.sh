#!/bin/sh

mkdir -p ${DJANGO_STATIC_ROOT} && chown estiamadm:www-data ${DJANGO_STATIC_ROOT}
mkdir -p ${DJANGO_MEDIA_ROOT} && chown estiamadm:www-data ${DJANGO_MEDIA_ROOT}
mkdir -p ${POSTGRES_DATA} && chown estiamadm:www-data ${POSTGRES_DATA}

python manage.py makemigrations && python manage.py migrate --noinput
python manage.py  collectstatic --noinput

echo "Server starting at port ${DJANGO_DEV_SERVER_PORT}....."
USER_EXISTS="from django.contrib.auth import get_user_model; User = get_user_model(); exit(User.objects.exists())"
python manage.py shell -c "$USER_EXISTS" && python manage.py createsuperuser --noinput
exec gosu estiamadm uwsgi --http-socket :${DJANGO_DEV_SERVER_PORT} --uid estiamadm --ini server_config/docker.ini --processes 4 --threads 2 --wsgi-file user_management_service/wsgi.py
