#!/bin/bash
set -e

if [ "$(cat /proc/sys/kernel/yama/ptrace_scope)" -ne 0 ]; then
    echo "You need to set /proc/sys/kernel/yama/ptrace_scope to 0 for this challenge to work"
    exit 1
fi

chown root:root /etc /etc/sudoers.d /etc/sudoers.d/*
chmod -R 550 /etc/sudoers.d
chown -R root:root /home

useradd -d /home/$[USER] -s /bin/bash $[USER]
chown -R $[USER]:$[USER] /home/$[USER]

gcc /keyrecv.c -o /keyrecv && rm /keyrecv.c
chmod 755 /keyrecv

gcc /keysend.c -o /keysend && rm /keysend.c
chmod 700 /keysend