#!/bin/sh
set -e

chown root:root /etc

chown -R root:root /etc/ssh
chmod 600 /etc/ssh/ssh_host*

chown -R root:root /etc/sudoers.d
chmod 440 /etc/sudoers.d/*

chown -R root:root /home

sed -i 's/ENABLED=1/ENABLED=0/g' /etc/default/motd-news
chmod -x /etc/update-motd.d/*
rm /etc/legal

useradd -M -d /home/flag0 -s /home/flag0/forward-to-flag1.sh flag0
echo flag0:unitedctf | chpasswd
chown -R flag0:flag0 /home/flag0
chmod +x /home/flag0/forward-to-flag1.sh

useradd -M -G spawner -d /home/flag1 -s /home/flag1/forward-to-flag2.sh flag1
echo flag1:$[FLAG0] | chpasswd
chown -R flag1:flag1 /home/flag1
chmod +x /home/flag1/forward-to-flag2.sh

useradd -M -G spawner -d /tmp -s /forward-to-docker.sh flag2
echo flag2:$[FLAG1] | chpasswd

useradd -M -G spawner -d /tmp -s /forward-to-docker.sh flag3
echo flag3:$[FLAG2] | chpasswd

useradd -M -G spawner -d /tmp -s /forward-to-docker.sh flag4
echo flag4:$[FLAG3] | chpasswd

useradd -M -G spawner -d /tmp -s /forward-to-docker.sh flag5
echo flag5:$[FLAG4] | chpasswd

useradd -M -G spawner -d /tmp -s /forward-to-docker.sh flag6
echo flag6:$[FLAG5] | chpasswd