# Fichiers cachés

> Forensics

Author: [Alexandre-Xavier Labonté-Lamoureux (AXDOOMER)](https://github.com/axdoomer)

Voici un firmware open source pour un émetteur radio RC de type TX16S. Des truands l'ont modifié pour cacher des clés secrètes à l'intérieur, une façon ingénieuse pour que personne ne suspecte qu'ils s'échangeaient des données entre eux. 

L'utilitaire `binwalk` est très utile pour effectuer la tâche que vous devez accomplir.


## Setup

Requirements:
- `binwalk`

# Writeup

En faisant de la recherche sur Internet, on découvre qu'on peut extraire les fichiers avec le paramètre `-e`. 

`binwalk -e opentx-tx16s-en.bin`

On découvre un fichier ZIP intéressant dans les fichiers extraits. Celui-ci est protégé par un mot de passe qu'on n'a pas. Cependant, si on compare à la liste des signatures trouvées par `binwalk`, ce n'est pas tous les fichiers détectés qui ont été extraits. 

En faisant plus de recherche, on peut trouver l'existence du paramètre `--dd` qui permet de sélectionner les fichiers à extraire. On peut lui faire tout extraire. 

`binwalk --dd='.*' opentx-tx16s-en.bin`

On trouvera maintenant les images extraites. Une image de type GIF contient un code secret: `ajfqv3021mf-b9dj312kd0-3nac322p`

Si on utilise ce mot de passe sur le fichier ZIP, on peut extraire son contenu. Parmi les clés RSA, on trouve fichier texte contenant le flag `flag-223e55c67d3783f972ed42c0dfab8fad29085d6c`. 

