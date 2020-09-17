FROM mariadb:10.5

RUN apt-get update && apt-get -y install gettext-base \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

COPY ./init_env.sh /init_env.sh

CMD ["sh", "/init_env.sh"]
