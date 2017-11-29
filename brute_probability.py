from decimal import *
import sys
num_faces = long(sys.argv[1])
sum = 1L
i = 1
while i < num_faces:
	sum *= i
	i += 1

p = Decimal(sum) / Decimal(num_faces**num_faces)
print p
