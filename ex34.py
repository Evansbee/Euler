import math
from EvEuler import irange
factorials = []

for i in range(0,10):
   factorials.append(math.factorial(i))

max_factor = 0

max_digits = 1

while len(str(max_digits*math.factorial(9)))>max_digits:
   max_digits+=1


max_factor = math.factorial(9)*max_digits

for f in irange(max_factor):
   value = 0
   for d in str(f):
      value += factorials[int(d)]
   if value == f:
      print f
