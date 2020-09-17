# Captcha Reader

> Programming

Author: [Alexandre-Xavier Labonté-Lamoureux (AXDOOMER)](https://github.com/axdoomer)

Le but de ce défi est de lire le texte à l'intérieur d'un captcha. En vous connectant sur le socket, vous recevrez une image encodée en Base64 (les languages Python, JavaScript et Bash ont tous de quoi le décoder). Vous recevrez dix défis différents un après l'autre et devez renvoyer le texte lu au serveur sans erreur. Les caractères à décoder vont de 'a' à 'z', de 'A' à 'Z' et de '0' à '9'.

Vous pouvez trouver des bibliothèques, des API et d'autres outils d'OCR en cherchant sur Internet. Soyez ingénieux et utilisez les meilleurs outils que vous pouvez trouver. Vous n'avez que trois secondes pour décoder l'image et envoyer le résultat.

## Setup

Requirements:
- None

Start:

```
docker-compose up captcha-reader
```