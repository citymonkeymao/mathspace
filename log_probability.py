from decimal import *
import sys
num_faces = long(sys.argv[1])
from math import log, exp
log_sum = 0.0
i = 1
while i < num_faces:
	log_sum += log(i)
	i += 1
log_p = log_sum - num_faces * log(num_faces)
p = Decimal(log_p).exp()#exp(log_p)
print str.format('{0:.3000}',p)