thenumber = 600851475143
topfactor = 600851475143
factors = []

i = 2 

while i < topfactor:
   if thenumber % i == 0:
      factors.append(i)
      topfactor = thenumber/i;
   i = i + 1 


for i in factors:
   for j in factors:
      if i < j:
         if j % i == 0:
            factors.remove(j)


for factor in factors:
   print factor


