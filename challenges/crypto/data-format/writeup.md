# Writeup

Il est possible de réaliser chacune de ces opérations facilement avec CyberChef, avec To Hex, From Hex, To Base64, From Base64.

DECODE_HEX("464c4147") == "FLAG"
DECODE_BASE64("LTQ5NGM2Zjc2NjU0NDYxNw==") == "-494c6f766544617"
ENCODE_BASE64("461466f72") == "NDYxNDY2ZjcyNmQK"
ENCODE_HEX("6174730a") == "36313734373330610a"

Solution alternative: écrire un script python qui résout le challenge:

```python
import base64

a = bytes.fromhex("464c4147").decode()
b = base64.b64decode("LTQ5NGM2Zjc2NjU0NDYxNw==").decode()
c = base64.b64encode(b"461466f72").decode()
d = b"6174730a".hex()
print(a + b + c + d)
```

Réponse: FLAG-494c6f766544617NDYxNDY2Zjcy3631373437333061
