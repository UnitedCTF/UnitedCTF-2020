FROM python:3.6

RUN mkdir /app
WORKDIR /app

COPY ./requirements.txt /app/requirements.txt
RUN pip3 install -r /app/requirements.txt

COPY ./server.py /app/server.py
COPY ./flag.py /app/flag.py

ENTRYPOINT [ "python3", "server.py" ]
