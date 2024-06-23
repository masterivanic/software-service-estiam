#!/bin/sh

while ! PGPASSWORD=8Fny?aXEFkh9ePA3 psql -h ${POSTGRES_HOST} -U postgres -c '\q'; do echo "En attente du demarrage de postgresql..." && sleep 1; done
echo "BD demarré avec succès.......>>"
if ! PGPASSWORD=8Fny?aXEFkh9ePA3 psql -U postgres -h ${POSTGRES_HOST} -p ${POSTGRES_PORT} -lqt | cut -d \| -f 1 | cut -d ' ' -f 2 | grep -q "^estiam_db$"; then
    PGPASSWORD=8Fny?aXEFkh9ePA3 createdb -U postgres -h ${POSTGRES_HOST} -p ${POSTGRES_PORT} estiam_db
else
    echo "La database existe déjà..."
fi

mkdir -p ${DJANGO_STATIC_ROOT} && chown estiamadm:www-data ${DJANGO_STATIC_ROOT}
mkdir -p ${DJANGO_MEDIA_ROOT} && chown estiamadm:www-data ${DJANGO_MEDIA_ROOT}
mkdir -p ${POSTGRES_DATA} && chown estiamadm:www-data ${POSTGRES_DATA}

python manage.py makemigrations && python manage.py migrate --noinput
python manage.py  collectstatic --noinput

echo "Server starting at port ${DJANGO_DEV_SERVER_PORT}....."
USER_EXISTS="from django.contrib.auth import get_user_model; User = get_user_model(); exit(User.objects.exists())"
python manage.py shell -c "$USER_EXISTS" && python manage.py createsuperuser --noinput
exec gosu estiamadm uwsgi --http-socket :${DJANGO_DEV_SERVER_PORT} --uid estiamadm --ini server_config/docker.ini --processes 4 --threads 2 --wsgi-file estiam_service/wsgi.py
