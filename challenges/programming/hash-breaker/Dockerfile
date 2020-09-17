FROM python:3.6

RUN mkdir /app
WORKDIR /app

COPY ./server.py /app/server.py

ENTRYPOINT [ "python3", "server.py" ]
