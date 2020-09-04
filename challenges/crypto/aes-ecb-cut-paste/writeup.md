# Writeup

Lorsqu'on se connecte au serveur, il nous affiche un menu avec plusieurs options:

```
ECB Crypto Menu
1. Encrypt data
2. Get flag
3. Exit

> Your choice:
```

On nous donne le choix de chiffrer des données. Essayons:

```
> Your choice: 1
> Enter your name: allo
Cookie: name=allo&flag=False
Ciphertext: 7a02ece63ea4bfd33e250aaead2d2c0610392930210e6642f3c8fe5377e0ef0f
```

Le serveur nous affiche donc un "cookie" qui contient simplement notre nom et une clé `flag` ayant la valeur `False`.

Pour obtenir le flag, il faudra changer la valeur de cette clé pour `True`.

On sait que le problème avec ECB vient du fait que les blocs sont tous chiffrés indépendamment les uns des autres. Cela veut dire qu'on peut réordonner les blocs sans briser le chiffrement.

Ainsi, il est possible de séparer les messages chiffrés en blocs et de réarranger ces blocs comme on veut pour créer un nouveau _ciphertext_ truqué. Dans ce cas-ci, ce que l'on cherche à créer est un _ciphertext_ contenant l'entrée `flag=True`. Pour ce faire, il va falloir:

1. Utiliser le point d'entrée qu'on a (le nom) pour créer un bloc chiffré commençant par `True&`
2. Utiliser le point d'entrée pour créer un bloc terminant par `&flag=`

Ensuite, nous pourrons combiner les deux blocs, ce qui nous donnera le texte `&flag=True&` dans notre cookie:

```
Étape 2           Étape 1
XXXXXXXXXXXXXXXX YYYYYYYYYYYYYYYY
..........&flag= True&...........
```

Pour la première étape, il faut s'assurer que tout ce qui vient avant `True` soit dans un bloc précédent. Sachant que le cookie commence toujours par `name=` (5 caractères), nous devons mettre 11 caractères de texte avant la valeur `True`. Prenons donc le nom `alloaaaaaaaTrue`.

```
> Your choice: 1
> Enter your name: alloaaaaaaaTrue
Cookie: name=alloaaaaaaaTrue&flag=False
Ciphertext: a6a990542c9d4a8be385c431888a5f757d602bfe9da07b23f4bb173668fe0480
```

Nous pouvons séparer le texte chiffré en 2 blocs AES:

```
n a m e = a l l o a a a a a a a  T r u e & f l a g = F a l s e [padding]
a6a990542c9d4a8be385c431888a5f75 7d602bfe9da07b23f4bb173668fe0480
```

Comme prévu, on a bel et bien un bloc commençant par `True&`!

Si nous pouvons faire en sorte de générer un bloc qui se termine par `&flag=` et que nous insérons ensuite le bloc chiffré commençant par `True&`, alors le serveur va penser que ce cookie possède comme entrée `flag=True`, ce qui nous permettra d'obtenir le flag!

Sachant que le cookie débute par `name=` (5 caractères) et qu'on veut qu'il se termine par `&flag=` (6 caractères), cela nous laisse 5 caractères pour notre nom. Avec le nom `aaaaa`, le premier bloc chiffré sera `name=aaaaa&flag=` (16 caractères exactement):

```
> Your choice: 1
> Enter your name: aaaaa
Cookie: name=aaaaa&flag=False
Ciphertext: d60c85b76c8d3d5083bf9a04f69f7e1c9d6ad7a322cbcb7143c0f960a48ee87e
```

Séparons ce texte chiffré en blocs:

```
n a m e = a a a a a & f l a g =  F a l s e [padding]
d60c85b76c8d3d5083bf9a04f69f7e1c 9d6ad7a322cbcb7143c0f960a48ee87e
```

Nous pouvons maintenant mélanger les blocs obtenus à l'étape 1 et à l'étape 2 pour obtenir un nouveau cookie qui est valide, mais qui n'a jamais été créé par le serveur lui-même:

```
Étape 2                          Étape 1
n a m e = a a a a a & f l a g =  T r u e & f l a g = F a l s e [padding]
d60c85b76c8d3d5083bf9a04f69f7e1c 7d602bfe9da07b23f4bb173668fe0480
```

Ce cookie contient deux entrées `flag`, une valant `True` et l'autre valant `False`. Puisque le serveur ne fait pas de validation pour ce genre d'incohérence, le flag sera affiché lorsque l'entrée `flag=True` sera lue.

Envoyons ce nouveau cookie au serveur en collant les deux blocs ensemble:

```
> Your choice: 2
> Enter your cookie: d60c85b76c8d3d5083bf9a04f69f7e1c7d602bfe9da07b23f4bb173668fe0480
FLAG-32c2a2f6befcf9bb7ad9e9e359e550b2
```
