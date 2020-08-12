FROM node:dubnium AS build

WORKDIR /app
RUN chown node:node /app
USER node

COPY --chown=node:node . /app

RUN node build.js ./root

FROM unitedctf-sysadmin-base

COPY --from=build /app/build/root /
RUN sh < /perms.sh && rm /perms.sh