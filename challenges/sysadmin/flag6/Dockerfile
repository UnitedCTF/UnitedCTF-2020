FROM node:dubnium AS build

WORKDIR /app
RUN chown node:node /app
USER node

COPY --chown=node:node . /app

RUN node build.js ./root

FROM ubuntu:18.04

RUN apt update
RUN apt install -y \
    netcat net-tools \
    python python3 \
    build-essential \
    sudo bash-completion curl wget htop \
    nano vim man git

RUN git clone https://github.com/vuejs/vue --depth=1 /repos/vue
RUN rm -rf /repos/vue/.git

RUN git clone https://github.com/facebook/react --depth=1 /repos/react
RUN rm -rf /repos/react/.git

RUN git clone https://github.com/angular/angular --depth=1 /repos/angular
RUN rm -rf /repos/angular/.git /repos/angular/aio /repos/angular/packages

RUN git clone https://github.com/emberjs/ember.js --depth=1 /repos/emberjs
RUN rm -rf /repos/emberjs/.git

RUN git clone https://github.com/meteor/meteor --depth=1 /repos/meteor
RUN rm -rf /repos/meteor/.git

COPY --from=build /app/build/root /
RUN sh < /perms.sh && rm /perms.sh
