FROM python:3.6

RUN mkdir /app
WORKDIR /app

COPY ./requirements.txt /app/requirements.txt
RUN pip3 install -r /app/requirements.txt

COPY ./server.py /app/server.py
COPY ./random.png /app/random.png
COPY ./Roboto-Regular.ttf /app/Roboto-Regular.ttf

ENTRYPOINT [ "python3", "server.py" ]
