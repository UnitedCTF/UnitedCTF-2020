#!/bin/bash
set -e

chown -R root:root /home

useradd -d /home/$[USER1] -c $[FLAG3] -s /bin/bash $[USER1]
echo $[USER1]:$[PASS1] | chpasswd
chown -R $[USER1]:$[USER1] /home/$[USER1]