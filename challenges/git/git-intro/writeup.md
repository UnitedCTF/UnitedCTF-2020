# Partie 1
Le flag a simplement été supprimé du dossier. Un simple `git reset HEAD --hard` le ramènera:

`FLAG-4b47f5c0299bfcffef9b825732db30ff`

# Partie 2
En faisant `git log`, on s'aperçoit qu'un des messages de commit contient un flag:

`FLAG-5562b3bbe01d1c6348ac6587909d0328`

# Partie 3
En faisant `git branch`, on voit qu'il y a une branche qui s'appelle `new-flag`. On fait `git checkout new-flag` pour aller sur cette branche on ouvre le fichier `flag` pour voir son nouveau contenu:

`FLAG-0f933ce5cb1d769d153fc16a53c36cd7`

# Partie 4
En faisant `git stash list`, on voit qu'il y a quelque chose dans le `stash`:

```
$ git stash list
stash@{0}: WIP on master: f929acf Add .gitignore
```

En faisant `git stash pop` ou `git stash apply`, on voit que le fichier `flag.png` se modifie. En ouvrant l'image, on trouve le flag suivant:

`FLAG-88cd8162dc988ef495fcd8652e405ff9`
