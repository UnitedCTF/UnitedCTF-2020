#!/bin/bash
set -e

dd if=/dev/random of=/tmp/secret bs=4096 count=1 &>/dev/null

FLAG=$(openssl enc -aes-256-cbc -d -pbkdf2 -iter 100000 -salt -md sha512 -pass file:/home/secretuser/secret -in /home/secretuser/flag.enc -out -)
echo $FLAG | openssl enc -aes-256-cbc -pbkdf2 -iter 100000 -salt -md sha512 -pass file:/tmp/secret -in - -out /home/secretuser/flag.enc

mv /tmp/secret /home/secretuser/secret
chmod 600 /home/secretuser/secret