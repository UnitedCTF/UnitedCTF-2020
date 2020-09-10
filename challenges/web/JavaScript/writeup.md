# Writeup

## Login 1

- `FLAG-e7ebfbb9dcf5cfb60ae1bb59d40f7695`

Pour voir le drapeau il suffit d'évaluer la chaîne de caractères `"\x46\x4c\x41\x47\x2d\x65\x37\x65\x62\x66\x62\x62\x39\x64\x63\x66\x35\x63\x66\x62\x36\x30\x61\x65\x31\x62\x62\x35\x39\x64\x34\x30\x66\x37\x36\x39\x35"` dans la console du navigateur. 

## Login 2

- `FLAG-1fbeb0a21f8d1286086ca419079c62f8a`

Avant tout il faut comprendre ce que le code JavaScript fait, pour ce faire on indente correctement le script, puis on renomme les fonctions et variables.

Par la suite il faut programmer une solution qui fait l'inverse de la fonction d'encryption.

Voici une solution qui affiche le drapeau dans la console du navigateur, lorsqu'exécutée dans celle-ci.

```js
var cipher = "NzE6NzQ6Njc6Nzg6NDM6NTY6OTY6MjoxMDU6Nzo1MzoxMDU6NTA6NTY6OTg6NTE6OTg6ODM6NDg6OTc6NTU6NTQ6NTY6NjU6MTA1OjEwNDo1MDo4Mzo2MTo4OTo1Mjo2NToxMDE6NjU6NTQ6MTEzOjYyOjM";
var key = "2718587a3f";

function keyValueAt(key, index) {
  var value;
  var keyIndex = index % key.length;
  var integer = parseInt(key[keyIndex]);
  if (integer && !isNaN(integer)) {
    value = integer;
  } else {
    value = key.charCodeAt(keyIndex);
  }
  return value;
}

function decrypt(key, cipherBase64) {
  var plaintext = '';
  var cipher = atob(cipherBase64).split(':');

  for (let i = 0; i < cipher.length; i++) {
    var code = parseInt(cipher[i]);
    if (code % 2 == 0) {
      code = code + 1;
    } else {
      code = code - 3;
    }
    var char = String.fromCharCode(code ^ keyValueAt(key, i));
    plaintext += char;    
  }

  return plaintext;
}

console.log(decrypt(key, cipher));
```

