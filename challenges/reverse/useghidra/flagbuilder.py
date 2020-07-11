import random

flag = "flag-n0tw3llH1dd3nIsn7i7"

array1 = []
array2 = []

for c in flag:
	index = ord(c)
	first_val = random.randrange(1, index)
	second_val = index - first_val

	array1.append(first_val)
	array2.append(second_val)

print(', '.join([hex(i) for i in array1]))
print(', '.join([hex(i) for i in array2]))
