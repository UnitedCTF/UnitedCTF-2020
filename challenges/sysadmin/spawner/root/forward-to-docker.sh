#!/bin/bash

if [ ! -t 1 ]; then
    echo "Ne vous compliquez pas la vie en enlevant le TTY :p" | cowsay
    echo
    exit 0
elif [ ! -z "$1" ]; then
    echo "Pas besoin de commande pour vous connecter en SSH ;)" | cowsay
    echo
    exit 0
fi

sudo -u root /spawner.sh "$(id -un)"