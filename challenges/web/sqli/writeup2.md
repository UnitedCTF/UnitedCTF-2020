# Writeup - Injection SQL #2: ERREUR: TITRE INVALIDE

La requête pour ce défi est:

```sql
SELECT id,flag FROM challenge2 WHERE id='NOTRE_INPUT';
```

Cette fois, les résultats de la requête ne nous sont pas montrés. Par contre, les messages d'erreurs sont toujours affichés et le nom des colonnes nous est donné dans la requête. Notre but est d'utiliser ces messages d'erreur pour exfiltrer l'information qui nous intéresse: la colonne `flag`. Il existe d'autres manières possible pour résoudre ce défi, mais celle-ci est la plus simple. Nous verrons les autres techniques dans les défis suivants.

Il y a plusieurs moyens de créer volontairement des erreur dans nos requêtes SQL qui afficheront des données. Une recherche pour "error based sql injection" en sort une grande variété. Ici, nous utiliserons la fonction `extractvalue`.

`extractvalue` prend 2 paramètres, un object XML et une expression XPath (vous n'avez pas besoin de connaître ces concepts pour l'utiliser ici). En donnant une expression XPath invalide, le message d'erreur nous affiche le début de cette expression. Si on la construit en utilisant une sous-requête qui donne l'information recherchée, on peut donc voir cette information dans l'erreur:

```sql
 -- Notre entrée
' UNION SELECT extractvalue('', concat(':',(select flag from challenge2))) -- 
 -- Requête complète
SELECT id,flag FROM challenge2 WHERE id='' UNION SELECT extractvalue('',concat(0x3a,(select flag from challenge2))) -- ';
```

Et le message d'erreur qui nous est affiché contient le flag: `XPATH syntax error: ':FLAG-Ash_nazg_durbatuluk_Hl4z'`
