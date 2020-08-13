#!/bin/bash
set -e

chown -R root:root /home

useradd -d /home/$[USER] -s /bin/bash $[USER]
chown -R $[USER]:$[USER] /home/$[USER]

useradd -d /home/secretuser -s /bin/bash secretuser
chown -R secretuser:secretuser /home/secretuser