from decimal import *
import sys
num_faces = long(sys.argv[1])
from math import log, exp
sum=reduce(lambda x,y:x*y,range(1,num_faces))
p = Decimal(sum) / Decimal(num_faces**num_faces)
print p
# log_sum = 0
# i = 0
# while i < num_faces:
# 	log_sum += log(i)
# log_p = log_sum - num_faces * log(num_faces)
# p = exp(log_p)