FROM node:dubnium AS build

WORKDIR /app
RUN chown node:node /app
USER node

COPY --chown=node:node . /app

RUN node build.js ./root

FROM ubuntu:20.04

RUN apt update
RUN apt install -y \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common

RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -
RUN add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
RUN apt install -y docker-ce

RUN apt install -y ssh net-tools sudo cowsay 

COPY --from=build /app/build/root /
RUN chmod +x /*.sh && chown root:root /*.sh 

RUN groupadd spawner

RUN sh < /perms.sh && rm /perms.sh
ENTRYPOINT [ "/entrypoint.sh" ]