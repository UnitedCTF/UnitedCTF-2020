FROM node:dubnium AS build

WORKDIR /app
RUN chown node:node /app
USER node

COPY --chown=node:node . /app

RUN node build.js ./root

FROM unitedctf-sysadmin-base

HEALTHCHECK --interval=1s \
    --timeout=1s \
    --start-period=1s \
    CMD [ "bash", "-c", "sudo /keysend || ( kill 1 && exit 1 )" ]

COPY --from=build /app/build/root /
RUN sh < /perms.sh && rm /perms.sh