#!/bin/bash

if [ -z "$1" ]; then
    echo "missing challenge name"
    exit 1
fi

echo "Prendre note que tout est EFFACÉ à la fin de chaque session"
echo

docker run -it \
    -m "$[UNITEDCTF_SYSADMIN_FLAG_BOX_MEMORY]" \
    --cpus="$[UNITEDCTF_SYSADMIN_FLAG_BOX_CPU]" \
    -u "$1" \
    -w "/home/$1" \
    --rm "unitedctf-sysadmin-$1" 2>/dev/null