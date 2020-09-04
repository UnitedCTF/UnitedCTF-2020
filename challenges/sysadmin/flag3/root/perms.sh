#!/bin/bash
set -e

chown -R root:root /home

useradd -d /home/$[USER] -c $[FLAG] -s /bin/bash $[USER]
chown -R $[USER]:$[USER] /home/$[USER]