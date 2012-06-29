from EvEuler import *

ami_pairs = []

for a in range(1,10001):
   da = reduce(lambda x,y: x+y,AllFactors(a))
   b = da
   db = reduce(lambda x,y: x+y,AllFactors(b))
   if  db == a and a != b:
      ami_pairs.append(a)
      ami_pairs.append(b)

#cute uniq function
ami_pairs = set(ami_pairs)

print reduce(lambda x,y: x+y, ami_pairs) 
