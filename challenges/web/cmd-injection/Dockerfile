FROM python:3.6

RUN mkdir /app
WORKDIR /app

COPY ./requirements.txt /app/requirements.txt
RUN pip3 install -r /app/requirements.txt

COPY ./app.py /app/app.py
COPY ./flag /app/flag
COPY ./static /app/static/
COPY ./templates /app/templates/

USER 1000
ENTRYPOINT [ "flask", "run", "--host", "0.0.0.0" ]
