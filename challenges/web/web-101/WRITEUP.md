# Writeup

## Flag 1

- `FLAG-03f06d335e77ccba975315b27a5e4493`

Le premier drapeau ce trouve dans le code source HTML de la page.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>My Awesome Blog</title>
</head>
<body>
  <!-- This is HTML comment. -->
  <!-- Sometimes is contains important information that the programmer might have left. -->
  <h1>My Awesome Blog</h1>
  <p>Hi, my name is John Doe! I love cats, programming and also flags.</p>
  <hr>
      <h2>Posts</h2>
    <ul>
      <li><a href='?id=1'>Let's reinvent the wheel!</a></li>
<li><a href='?id=2'>Programming is my passion</a></li>
<li><a href='?id=4'>Cat, the king of the animal kingdom</a></li>
<li><a href='?id=5'>I thought robots were all made from metal.</a></li>
    </ul>
    <footer>© My Awesome Blog</footer>
  <!-- Secret Flag 1: FLAG-03f06d335e77ccba975315b27a5e4493 -->
</body>
</html>
```

## Flag 2

- `FLAG-4394bca60851f3abdd85c27cd23f93a4`

Le second drapeau est accessible via l'article de blog avec l'identifiant _4_. Il est possible de le deviner en visitant les autres articles de blog et de voir que le paramètre de requête `id` containt les valeurs de 1 à 5, mais pas 3. Il suffit de mettre `id=3` pour obtenir le drapeau dans le contenu de l'article.

- [http://127.0.0.1:12000/?id=3](http://127.0.0.1:12000/?id=3)

```html
<h2>Secret Flag 2</h2>
<p>FLAG-4394bca60851f3abdd85c27cd23f93a4</p>
```

## Flag 3

- `FLAG-4394bca60851f3abdd85c27cd23f93a4`

L'article de blog 5 (http://127.0.0.1:12000/?id=5) expliquait qu'il exsite des « web robots » avec un lien qui explique qu'il suffit de mettre un fichier `/robots.txt` pour les empêcher d'indexer certain page.

En visitant le fichier `/robots.txt` on voit que le fichier `/this-is-the-secret-flag-3.txt` est marqué pour ne pas être indexer par les robots du web. En visitant ce fichier on obtient le drapeau.

## Flag 4

- `FLAG-6a11afa3a060b06ac714a2f38d6b7147`

L'article de blog 2 (http://127.0.0.1:12000/?id=2) expliquait qu'il est possible en PHP de retourner des entête HTTP non-standard.

Il suffit de regarder les entête HTTP à l'aide de l'inspecteur de requête de votre navigateur ou en utilisant un proxy comme BurpSuite.

```
X-Secret-Flag-4: FLAG-6a11afa3a060b06ac714a2f38d6b7147
```

## FLAG 5

- `FLAG-9fd42bed331fdbc7346c1b7a02043919`

L'article de blog 5 (http://127.0.0.1:12000/?id=5) expliquait qu'il exsite des « web robots » avec un lien qui explique qu'il suffit de mettre un fichier `/robots.txt` pour les empêcher d'indexer certain page.

En visitant le fichier `/robots.txt` on voit que le fichier `secret-stuff-only-for-admin-stuff/index.php` est marqué pour ne pas être indexer par les robots du web. 

En visitant cette page fichier on regarde le code source on voit comment utiliser le mode « debug ».

```html

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>My Awesome Blog | Admin section</title>
</head>
<body>
  <h1>My Awesome Blog | <u>Admin section</u></h1>
  <p>This is in beta.</p>
  <p>This is to help admin debug the code source of a <i>page</i>.</p>
  <hr>
  <h4>Admin Pages:</h4>
  <ul>
    <li>
      <a href="index.php">index.php</a>
    </li>
    <li>
      <a href="test.php">test.php</a>
    </li>
    <!-- TODO: List the other pages. -->
  </ul>
  <hr>
  <code>
    <!-- To use the debug mode specify the page. -->
    <!-- Example: ?page=test.php -->
    </code>
  <hr>
  <footer>© My Awesome Blog</footer>
</body>
</html>

```

En visitant le `/secret-stuff-only-for-admin-stuff/index.php?page=index.php` on peut voir le code source PHP de la page qui contient le drapeau.

```php
  // I heard this could cause a security vulnerability called: Local File Inclusion (LFI).
  // This is way for now we can only see file in this directory.
  // Secret Flag 5: FLAG-9fd42bed331fdbc7346c1b7a02043919
  $pages = array("index.php", "test.php");
  if (isset($_GET['page']) && in_array($_GET['page'], $pages)) {
    highlight_string(file_get_contents($_GET['page']));
  }
```

