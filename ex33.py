from EvEuler import irange

ansnum = []
ansdem = []

for num in irange(10,98):
   for den in irange(num+1,99):
      #throw out the goofy cases
      if num == den:
         continue
      if num % 10 == 0 or den % 10==0:
         continue

      n1,n2 = num / 10, num % 10
      d1,d2 = den / 10, den % 10

      if n1 != n2 and d1 != d2 and (n1 == d2 or n2 == d1):
         if float(n1)/float(d2) == float(num)/float(den) or float(n2)/float(d1) == float(num)/float(den):
            
            
            print "%d/%d"%(num,den)

