#!/bin/bash

# Start the SSH service
/etc/init.d/ssh start

# Correct the docker group id to match the host
if [ "$(stat /var/run/docker.sock --format='%G')" != "docker" ]; then
    docker_id=$(stat /var/run/docker.sock --format='%g')
    groupmod -g $docker_id docker
fi

# Display the network interfaces
ifconfig

while :; do
    sleep Infinity
done