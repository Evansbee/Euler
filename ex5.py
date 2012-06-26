from EvEuler import *

primeslist=[]

for i in range (1,20):
   primeslist.append(PrimeFactors(i))

commonprimefactors = []

for i in primeslist:
   for j in i:
      while i.count(j) > commonprimefactors.count(j):
         commonprimefactors.append(j)

number = 1

for i in commonprimefactors:
   number = number * i;

print number
