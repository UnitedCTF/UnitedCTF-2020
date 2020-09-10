#!/bin/bash

pattern="(s|m|c|r|b|u|g|w|x|d|\?|\*|-|\||\`|>|<|\"|\!|\.)"
if [[ $1 =~ [^A-z0-9] ]] || [ ! -x "/bin/$1" ]; then
    echo -e "\e[91mEXÉCUTABLE INVALIDE\e[0m"
    exit 1
elif [[ $@ =~ secret(user)? ]]; then
    echo -e "\e[91mSECRET DÉTECTÉ\e[0m"
    exit 1
elif [[ $@ =~ $pattern ]]; then
    echo -e "\e[91mCARACTÈRE BANNI\e[0m"
    exit 1
fi

# bloquer tout output pour un maximum de protection
eval "/bin/$1" "${@:2}" &>/dev/null