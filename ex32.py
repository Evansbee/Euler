#1*3?5N
#1*4?4Y
#1*5?3N

#2*2?5N
#2*3?4Y
#2*4?3N
from EvEuler import irange

pds = []
total = 0
def IsPandigital(numstring):
   for i in irange(1,9):
      if numstring.count(str(i))!=1:
         return False
   return True

for a in irange(1,9):
   for b in irange(1234,9876):
      c = a*b
      if len(str(c)) == 4 and IsPandigital(str(a)+str(b)+str(c)):
         pds.append(c)
         print "%d * %d = %d"%(a,b,c)


for a in irange(12,98):
   for b in irange(123,987):
      c = a*b
      if len(str(c))==4 and IsPandigital(str(a)+str(b)+str(c)):
         pds.append(c)
         print "%d * %d = %d"%(a,b,c)
pds = set(pds)
for i in pds:
   total+=i
print total
