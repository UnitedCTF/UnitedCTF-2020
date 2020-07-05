#!/bin/bash

echo "Prendre note que tout est EFFACÉ à la fin de la session"
docker run -it \
    -m "$[UNITEDCTF_SYSADMIN_FLAG_BOX_MEMORY]" \
    --cpus="$[UNITEDCTF_SYSADMIN_FLAG_BOX_CPU]" \
    -u $[USER1] \
    -w /home/$[USER1] \
    --rm $[UNITEDCTF_SYSADMIN_FLAG_BOX_NAME]