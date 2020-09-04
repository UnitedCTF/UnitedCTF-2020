#!/bin/bash
set -e

chown -R root:root /home

mv /repos/* /home/$[USER]
rmdir /repos

useradd -d /home/$[USER] -s /bin/bash $[USER]
chown -R $[USER]:$[USER] /home/$[USER]

echo -e "\n$[FLAG]" >> /home/$[USER]/react/packages/react/src/React.js