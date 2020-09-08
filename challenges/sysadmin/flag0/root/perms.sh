#!/bin/bash
set -e

chown -R root:root /home

chmod +x /entrypoint.sh
chown root:root /entrypoint.sh

useradd -d /home/$[USER] -s /bin/bash $[USER]
chown -R $[USER]:$[USER] /home/$[USER]