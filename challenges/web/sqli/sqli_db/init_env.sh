#!/bin/sh

for f in /init_sql/*.sql; do
	envsubst < $f > "/docker-entrypoint-initdb.d/$(basename $f)"
done

# Call mariadb entrypoint
docker-entrypoint.sh mysqld
