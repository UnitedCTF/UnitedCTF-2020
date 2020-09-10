#!/bin/sh
set -e

groupadd spawner

chmod +x /*.sh
chown root:root /etc

chown -R root:root /etc/ssh
chmod 600 /etc/ssh/ssh_host*

chown -R root:root /etc/sudoers.d
chmod 440 /etc/sudoers.d/*

chown -R root:root /home

sed -i 's/ENABLED=1/ENABLED=0/g' /etc/default/motd-news
chmod -x /etc/update-motd.d/*
rm /etc/legal

useradd -M -G spawner -d /home/flag0 -s /forward-to-docker.sh flag0
chown -R flag0:flag0 /home/flag0
echo flag0:unitedctf | chpasswd

useradd -M -G spawner -d /home/flag1 -s /forward-to-docker.sh flag1
chown -R flag1:flag1 /home/flag1

useradd -M -G spawner -d /home/flag2 -s /forward-to-docker.sh flag2
chown -R flag2:flag2 /home/flag2

useradd -M -G spawner -d /home/flag3 -s /forward-to-docker.sh flag3
chown -R flag3:flag3 /home/flag3

useradd -M -G spawner -d /home/flag4 -s /forward-to-docker.sh flag4
chown -R flag4:flag4 /home/flag4

useradd -M -G spawner -d /home/flag5 -s /forward-to-docker.sh flag5
chown -R flag5:flag5 /home/flag5

useradd -M -G spawner -d /home/flag6 -s /forward-to-docker.sh flag6
chown -R flag6:flag6 /home/flag6

useradd -M -G spawner -d /home/flag7 -s /forward-to-docker.sh flag7
chown -R flag7:flag7 /home/flag7

useradd -M -G spawner -d /home/flag8 -s /forward-to-docker.sh flag8
chown -R flag8:flag8 /home/flag8

useradd -M -G spawner -d /home/flag9 -s /forward-to-docker.sh flag9
chown -R flag9:flag9 /home/flag9