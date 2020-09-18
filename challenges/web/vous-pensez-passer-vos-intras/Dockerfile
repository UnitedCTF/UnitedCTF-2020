FROM ubuntu:20.04

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update
RUN apt-get -y install maven mysql-server

COPY ./ /tmp/src
WORKDIR /tmp/src
RUN mvn clean install
EXPOSE 8080

ENTRYPOINT ["bash", "run.sh"]
