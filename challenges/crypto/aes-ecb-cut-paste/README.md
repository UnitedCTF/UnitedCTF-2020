# AES ECB Cut & Paste

> Crypto

Author: @xshill

Le mode de chiffrement ECB est reconnu pour être très peu sécuritaire. Le problème avec ECB est que tous les blocs chiffré sont indépendants les uns des autres, ce qui veut dire que:

1. Tous les blocs de _plaintext_ identiques auront des _ciphertext_ identiques
2. Les blocs peuvent être réarrangés

Par exemple, si on chiffre `TheQuickBrownFox` avec la clé `alloalloalloallo`, on obtient le _ciphertext_ suivant:

```
T h e Q u i c k B r o w n F o x  (bloc vide)
440f4cad6709f924e8ad521119632484 2736de5ffed3d1a7ea46b436d37de6e4
```

> [Lien CyberChef](https://gchq.github.io/CyberChef/#recipe=AES_Encrypt(%7B'option':'UTF8','string':'alloalloalloallo'%7D,%7B'option':'Hex','string':''%7D,'ECB','Raw','Hex')&input=VGhlUXVpY2tCcm93bkZveA)

Si on chiffre `TheQuickBrownFoxTheQuickBrownFox` avec la même clé, on obtient le _ciphertext_ suivant:

```
T h e Q u i c k B r o w n F o x  T h e Q u i c k B r o w n F o x  (bloc vide)
440f4cad6709f924e8ad521119632484 440f4cad6709f924e8ad521119632484 2736de5ffed3d1a7ea46b436d37de6e4
```

> [Lien CyberChef](https://gchq.github.io/CyberChef/#recipe=AES_Encrypt(%7B'option':'UTF8','string':'alloalloalloallo'%7D,%7B'option':'Hex','string':''%7D,'ECB','Raw','Hex')&input=VGhlUXVpY2tCcm93bkZveFRoZVF1aWNrQnJvd25Gb3g)

Comme vous pouvez le voir, les deux premiers blocs sont identiques, car ils ont un _plaintext_ identique.

Si on chiffre cette fois `TheQuickBrownFoxTheSlowOrangeCat`, le résultat est:

```
T h e Q u i c k B r o w n F o x  T h e S l o w O r a n g e C a t  (bloc vide)
440f4cad6709f924e8ad521119632484 2b3ea5ceb6d4e1a4b14d8da8317107c2 2736de5ffed3d1a7ea46b436d37de6e4
```

> [Lien CyberChef](https://gchq.github.io/CyberChef/#recipe=AES_Encrypt(%7B'option':'UTF8','string':'alloalloalloallo'%7D,%7B'option':'Hex','string':''%7D,'ECB','Raw','Hex')&input=VGhlUXVpY2tCcm93bkZveFRoZVNsb3dPcmFuZ2VDYXQ)

Puisque les blocs sont indépendants, on peut interchanger les deux premiers blocs et le déchiffrement fonctionnera quand même:

```
T h e S l o w O r a n g e C a t  T h e Q u i c k B r o w n F o x  (bloc vide)
2b3ea5ceb6d4e1a4b14d8da8317107c2 440f4cad6709f924e8ad521119632484 2736de5ffed3d1a7ea46b436d37de6e4
```

> [Lien CyberChef](https://gchq.github.io/CyberChef/#recipe=AES_Decrypt(%7B'option':'UTF8','string':'alloalloalloallo'%7D,%7B'option':'Hex','string':''%7D,'ECB','Hex','Raw',%7B'option':'Hex','string':''%7D)&input=MmIzZWE1Y2ViNmQ0ZTFhNGIxNGQ4ZGE4MzE3MTA3YzIgNDQwZjRjYWQ2NzA5ZjkyNGU4YWQ1MjExMTk2MzI0ODQgMjczNmRlNWZmZWQzZDFhN2VhNDZiNDM2ZDM3ZGU2ZTQ)

# Setup

Requirements:
- None

Start:

```
docker-compose up aes-ecb-cut-paste
```
