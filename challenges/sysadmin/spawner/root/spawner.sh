#!/bin/bash

if [ -z "$1" ]; then
    echo "missing challenge name"
    exit 1
fi

echo "Prendre note que tout est EFFACÉ à la fin de chaque session et que $[UNITEDCTF_SYSADMIN_FLAG_BOX_TMOUT] secondes d'inactivé met fin à la session"
echo

docker run -it \
    --name "unitedctf-sysadmin-$1-$(date +%s.%3N)" \
    -m "$[UNITEDCTF_SYSADMIN_FLAG_BOX_MEMORY]" \
    --cpus="$[UNITEDCTF_SYSADMIN_FLAG_BOX_CPU]" \
    --ulimit nproc="$[UNITEDCTF_SYSADMIN_FLAG_BOX_NPROC]" \
    -e "TMOUT=$[UNITEDCTF_SYSADMIN_FLAG_BOX_TMOUT]" \
    -u "$1" \
    -w "/home/$1" \
    --rm "unitedctf-sysadmin-$1" 2>/dev/null