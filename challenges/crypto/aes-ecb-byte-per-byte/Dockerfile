FROM ubuntu:18.04
RUN apt-get -y update
RUN apt-get -y install xinetd vim net-tools python3 python3-pip
RUN useradd challenge
RUN mkdir /app

WORKDIR /app

COPY ./config /etc/xinetd.d/pwn
COPY ./server.py /app/server.py
COPY ./flag.py /app/flag.py
COPY ./requirements.txt /app/requirements.txt

RUN pip3 install -r requirements.txt

CMD ["/usr/sbin/xinetd", "-dontfork"]
