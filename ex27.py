from EvEuler import *
stored_a,stored_b,stored_n = 0,0,0
pp = ListOfPrimesUnder(1000)
primes = []
for i in pp:
   primes.append(i)
   primes.append(0-i)

for a in primes:
   for b in primes:
      n = 0
      val = n * n
      val += a * n
      val += b
      while IsPrime(val):
         n += 1
         val = n * n
         val += a * n
         val += b
      if n > stored_n:
         stored_n = n
         stored_a = a
         stored_b = b


print "a: %d b: %d n: %d" % (stored_a,stored_b,stored_n)
print "axb: %d"%(stored_a*stored_b)
