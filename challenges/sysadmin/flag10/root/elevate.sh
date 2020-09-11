#!/bin/bash

# Mettre un filtre sur les commandes des utilisateurs qui n'ont pas le secret
if [ "$SECRET" != `cat /home/superuser/secret` ]; then
    if [[ $1 =~ [^A-z0-9] ]] || [ ! -x "/bin/$1" ]; then
        echo -e "\e[91mEXÉCUTABLE INVALIDE\e[0m"
        exit 1
    elif [[ $@ =~ secret(user)? ]]; then
        echo -e "\e[91mSECRET DÉTECTÉ\e[0m"
        exit 1
    elif [[ $@ =~ [axspduo\$\'\"\`\<\>\?\&\#] ]]; then
        echo -e "\e[91mCARACTÈRE BANNI\e[0m"
        exit 1
    fi
fi

# Bloquer toute entrée/sortie pour un maximum de protection
/bin/$1 "${@:2}" </dev/null &>/dev/null
exit 0