# Captcha Reader

> Programming

Author: [Alexandre-Xavier Labonté-Lamoureux (AXDOOMER)](https://github.com/axdoomer)

Le but de ce défi est de lire le texte à l'intérieur d'un captcha. En vous connectant sur le socket, vous recevrez la quantité d'octets à lire et l'image encodée en Base64 (les languages Python, JavaScript et Bash ont tous de quoi le décoder). Vous recevrez dix défis différents un après l'autre et devez renvoyer le texte lu au serveur sans erreur. Les caractères à lire dans l'image sont alphanumériques et certains caractères ambigus ont été enlevés pour réduire le risque d'erreurs. 

Vous pouvez trouver des bibliothèques, des API et d'autres outils d'OCR en cherchant sur Internet. Soyez ingénieux et utilisez les meilleurs outils que vous pouvez trouver. Vous n'avez que trois secondes pour décoder l'image et envoyer le résultat.

## Setup

Requirements:
- None

Start:

```
docker-compose up captcha-reader
```
