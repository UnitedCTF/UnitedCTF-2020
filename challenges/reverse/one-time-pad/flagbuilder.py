import random

flag = "flag-y0ur3aM4st3rp455w0rdd3cyph3r3r"

array1 = []
array2 = []

for c in flag:
	index = ord(c)
	first_val = random.getrandbits(8)
	while first_val == 0:
		first_val = random.getrandbits(8)

	second_val = first_val ^ ord(c)

	array1.append(first_val)
	array2.append(second_val)

print(', '.join([hex(i) for i in array1]))
print(', '.join([hex(i) for i in array2]))
