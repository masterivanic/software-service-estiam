#!/bin/sh

cp user_management_service/settings_docker_example.py user_management_service/settings_docker.py

mkdir -p ${DJANGO_STATIC_ROOT} && chown estiamadm:www-data ${DJANGO_STATIC_ROOT}
mkdir -p ${DJANGO_MEDIA_ROOT} && chown estiamadm:www-data ${DJANGO_MEDIA_ROOT}
mkdir -p ${POSTGRES_DATA} && chown estiamadm:www-data ${POSTGRES_DATA}

gosu estiamadm make migrate
gosu estiamadm make collectstatic

echo "Server starting at port ${DJANGO_DEV_SERVER_PORT}....."
USER_EXISTS="from django.contrib.auth import get_user_model; User = get_user_model(); exit(User.objects.exists())"
python manage.py shell -c "$USER_EXISTS" && python manage.py createsuperuser --noinput
exec gosu estiamadm uwsgi --http-socket :${DJANGO_DEV_SERVER_PORT} --uid estiamadm --ini server_config/docker.ini --processes 4 --threads 2 --wsgi-file user_management_service/wsgi.py
