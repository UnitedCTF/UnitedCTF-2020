# Initiation au JSON

> Programming

Author: @xshill

Maintenant que vous savez ouvrir des sockets, votre prochain défi est de réussir à implémenter un protocole réseau plus flexible. Pour cela, vous allez utiliser le format JSON!

Le JSON est un format de données très répandu. Il est facile à lire à l'oeil. [En voici des exemples](https://json.org/example.html).

## Les types de données primaires
Le JSON peut représenter des types de données comme les `string`, les entiers et les nombres à virgules:

```json
{
    "string": "Salut!",
    "age": 23,
    "ratio": 0.25
}
```

## Les tableaux
Les tableaux sont des collections de données mises entre crochets. Le type des données peut varier:

```json
{
    "array": [1, "deux", 3.0, 4]
}
```

## Les objets
Les objets JSON sont mis entre accolades, et contiennent des propriétés qui peuvent être des données de tous les types (y compris d'autres objets):

```json
{
    "nom": "Sylvain",
    "data": [1, 2, 3, 4, 5],
    "maison": {
        "adresse": "123 peel",
        "ville": "Montréal"
    }
}
```

## Le défi

Dans ce défi, le serveur vous envoie un objet JSON décrivant une personne, son enfant et son petit-enfant. Vous devez:
- Aller chercher l'objet du petit-enfant
- Ajouter la propriété `grandparent` avec comme valeur le nom de son grand-parent
- Envoyer cet objet avec sa nouvelle propriété au serveur

### Exemple: données du serveur
> Note: les noms seront remplacés par des noms aléatoires.

```json
{
    "name": "Grand-parent",
    "child": {
        "name": "Parent",
        // ...
        "child": {
            "name": "Petit-enfant"
            // ...
        }
    }
}
```

### Exemple: réponse au serveur
```json
{
    "name": "Petit-enfant",
    // ...
    // Autres propriétés de l'enfant envoyées par le serveur
    // ...
    "grandparent": "Grand-parent"
}
```

> Pour ce défi, n'implémentez pas votre propre décodeur de JSON. Cherchez plutôt une librairie à utiliser qui le fera à votre place. Ne réinventez pas la roue!

## Setup

Requirements:
- None

Start:

```
docker-compose up init-json
```
