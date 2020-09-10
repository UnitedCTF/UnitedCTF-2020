#!/bin/sh
set -e

groupadd spawner

chmod +x /*.sh
chown root:root /etc

chown -R root:root /etc/ssh
chmod 600 /etc/ssh/ssh_host*

chown -R root:root /etc/sudoers.d
chmod 440 /etc/sudoers.d/*

sed -i 's/ENABLED=1/ENABLED=0/g' /etc/default/motd-news
chmod -x /etc/update-motd.d/*
rm /etc/legal

echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDXMavX3kF2kZOub8ll93LST6BC/rfnq0LUcknLqQV1a2ppYnWoxwr5UfcvFahiVZcBU+FYIkRi93FkNxwhOATyOdCSTadE9c6EvzATRxADvphamqCzjfqVdD0I7xesLFDaTN1Jbr8qs6uJIze97A4gdgQitj58jvBCaHAtCuhP8uTOCQjOXoxspgQICT1dawZWfvGIFnUixT1VqZ3Pm3UgjmQhH0c65fQ4q1E3bAK+1NxexuaczSck70yNQ/+3OHvV55xMEkN/KjfGLzvU6UkGASdQm6nkuKPBLe3wEGi0hCfnZR4UORzo5646rDGfbn2XPb4P2ggOtrL8bla1B240QitjWnnUw8wbqLoYYAVXJGw9SxPjeW1nTBdrZSY08P9bazy7CyOs7UZWAoWdPlM8wahy2y8u0E5PH1PIq/VHJvfE53jhyZ68WqgDRMr1yvYBq3zy9e3C6tRUQDqiBf7IPU7/kN0LJHmEGkyCXmZ9AbU43YURN8nuhplFxKuwWH8= unitedctf" > /pubkey
for i in `seq 0 10`; do
    useradd -M -G spawner -d /home/flag$i -s /forward-to-docker.sh flag$i
    mkdir -p /home/flag$i/.ssh
    cp /pubkey /home/flag$i/.ssh/authorized_keys
    chown -R flag$i:flag$i /home/flag$i
done

echo flag0:unitedctf | chpasswd