#!/bin/bash
set -e

chown -R root:root /home

useradd -d /home/$[USER1] -c $[FLAG3] -s /bin/bash $[USER1]
chown -R $[USER1]:$[USER1] /home/$[USER1]

useradd -d /home/$[USER2] -s /bin/nologin $[USER2]
chown -R $[USER2]:$[USER2] /home/$[USER2]