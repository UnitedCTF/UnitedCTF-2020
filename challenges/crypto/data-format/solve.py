import base64

a = bytes.fromhex("464c4147").decode()
b = base64.b64decode("LTQ5NGM2Zjc2NjU0NDYxNw==").decode()
c = base64.b64encode(b"461466f72").decode()
d = b"6174730a".hex()
print(a + b + c + d)
