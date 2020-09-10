#!/bin/bash
set -e

chown root:root /etc /etc/sudoers.d /etc/sudoers.d/*
chmod -R 550 /etc/sudoers.d
chown -R root:root /home

useradd -d /home/$[USER] -s /bin/bash $[USER]
chown -R $[USER]:$[USER] /home/$[USER]

dd if=/dev/random of=/home/secretuser/secret bs=4096 count=1
echo "$[FLAG]" | \
    openssl enc -aes-256-cbc -pbkdf2 -iter 100000 -salt -md sha512 -pass file:/home/secretuser/secret -in - -out /home/secretuser/flag.enc

useradd -d /home/secretuser -s /bin/bash secretuser
chown -R secretuser:secretuser /home/secretuser
chmod 600 /home/secretuser/secret
chmod 744 /home/secretuser/rotatekeys.sh