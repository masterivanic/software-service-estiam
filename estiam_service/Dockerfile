FROM python:3.11.0

# Fixe le comportement du buffering
ENV PYTHONUNBUFFERED=1

# Définition du fuseau horaire
ENV TZ=Europe/Paris
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Création d'un groupe et d'un utilisateur, création du répertoire /app et installation des paquets nécessaires
RUN groupadd -r estiamadm && \
    useradd -r -m -g estiamadm estiamadm && \
    mkdir /app && \
    chown estiamadm /app && \
    apt-get update && \
    apt-get install -y locales postgresql-client locales-all python3-dev

# Définition des arguments de construction
ARG DJANGO_DEV_SERVER_PORT=8030
ARG POSTGRES_PORT=5432
ARG POSTGRES_HOST=db
ARG DJANGO_STATIC_ROOT=/var/www/static
ARG DJANGO_MEDIA_ROOT=/var/www/media
ARG POSTGRES_DATA=/var/lib/postgresql/data/

# Définition des variables d'environnement
ENV DJANGO_DEV_SERVER_PORT=$DJANGO_DEV_SERVER_PORT \
    DJANGO_STATIC_ROOT=$DJANGO_STATIC_ROOT \
    DJANGO_MEDIA_ROOT=$DJANGO_MEDIA_ROOT \
    POSTGRES_DATA=$POSTGRES_DATA \
    POSTGRES_PORT=$POSTGRES_PORT \
    POSTGRES_HOST=$POSTGRES_HOST \
    GOSU_VERSION=1.17

# Installation de gosu et d'autres outils nécessaires
RUN apt-get update && \
    apt-get install -y --no-install-recommends ca-certificates gnupg wget dos2unix && \
    rm -rf /var/lib/apt/lists/* && \
    dpkgArch="$(dpkg --print-architecture | awk -F- '{ print $NF }')" && \
    wget -O /usr/local/bin/gosu "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch" && \
    wget -O /usr/local/bin/gosu.asc "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch.asc" && \
    export GNUPGHOME="$(mktemp -d)" && \
    gpg --batch --keyserver hkps://keys.openpgp.org --recv-keys B42F6819007F00F88E364FD4036A9C25BF357DD4 && \
    gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu && \
    gpgconf --kill all && \
    rm -rf "$GNUPGHOME" /usr/local/bin/gosu.asc && \
    chmod +x /usr/local/bin/gosu && \
    gosu --version && \
    gosu nobody true

# Définition du répertoire de travail
WORKDIR /app

# Installation de poetry et d'uwsgi
RUN pip3 install poetry uwsgi

# Copie du code source et des fichiers de configuration
COPY . /app
COPY requirements.txt /app/requirements.txt

# Installation des dépendances Python
RUN pip3 install -r /app/requirements.txt

# Copie et préparation du script d'entrypoint
COPY entrypoint.sh /entrypoint.sh
RUN chown -R estiamadm:estiamadm /app && \
    tr -d '\r' < /entrypoint.sh > /tmp/entrypoint.sh && mv /tmp/entrypoint.sh /entrypoint.sh && \
    chmod +x /entrypoint.sh

# Définition de l'entrypoint et exposition du port
ENTRYPOINT ["/entrypoint.sh"]
EXPOSE $DJANGO_DEV_SERVER_PORT
