FROM mariadb:latest

RUN apt-get update && apt-get -y install gettext-base \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

COPY init_db.sql /tmp/
COPY .env /tmp/.env
RUN export $(cat /tmp/.env | xargs) && envsubst < /tmp/init_db.sql >/docker-entrypoint-initdb.d/init_db.sql
