FROM debian:stable-slim

RUN apt-get update && apt-get install -y xinetd && apt-get clean && rm -rf /var/apt/lists/*
RUN useradd -u 8888 -m molecule

CMD ["xinetd", "-dontfork"]
