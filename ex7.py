from EvEuler import *
primelist = []

i = 2

while len(primelist) < 10001:
   if len(PrimeFactors(i)) == 1:
      primelist.append(i)
      print "New prime (%d): %d" % (len(primelist), i)
   i = i + 1

print primelist[-1]
