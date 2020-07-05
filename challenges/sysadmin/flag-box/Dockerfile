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
    nano vim man

COPY --from=build /app/build/root /
RUN sh < /perms.sh && rm /perms.sh