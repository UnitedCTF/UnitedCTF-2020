#!/bin/sh
set -e

chown -R root:root /etc/ssh
chmod 600 /etc/ssh/ssh_host*

chown -R root:root /home

useradd -M -d /home/$[USER0] -s /home/$[USER0]/forward-to-user1.sh $[USER0]
echo $[USER0]:$[PASS0] | chpasswd
chown -R $[USER0]:$[USER0] /home/$[USER1]
chmod 755 /home/$[USER0]/forward-to-user1.sh

useradd -M -G docker -d /home/$[USER1] -s /home/$[USER1]/forward-to-flag-box.sh $[USER1]
echo $[USER1]:$[PASS1] | chpasswd
chown -R $[USER1]:$[USER1] /home/$[USER1]
chown root:root /home/$[USER1]/forward-to-flag-box.sh
chmod 755 /home/$[USER1]/forward-to-flag-box.sh

sed -i 's/ENABLED=1/ENABLED=0/g' /etc/default/motd-news
chmod -x /etc/update-motd.d/*

rm /etc/legal