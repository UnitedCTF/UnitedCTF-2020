#!/bin/bash
set -e

chown root:root /etc /etc/sudoers.d /etc/sudoers.d/*
chmod -R 550 /etc/sudoers.d
chown -R root:root /home

useradd -d /home/$[USER] -s /bin/bash $[USER]
chown -R $[USER]:$[USER] /home/$[USER]

useradd -d /home/superuser -s /bin/bash superuser
chown -R superuser:superuser /home/superuser
chmod 700 /home/superuser/secret.sh