from EvEuler import AllFactors
abundant_numbers = []
sums= []
for i in range(1,28124):
   f = AllFactors(i)
   if reduce(lambda x, y: x+y, AllFactors(i)) > i:
      abundant_numbers.append(i)
      print "%d - %r" %(i,f)
n_s_a = []

for i in abundant_numbers:
   for j in abundant_numbers[abundant_numbers.index(i):]:
      if i+j < 28124:
         sums.append(i+j) 

sums = set(sums)
for i in range(1, 28124):
   n_s_a.append(i)

for n in sums:
   n_s_a.remove(n)

print reduce(lambda x,y: x+y, n_s_a)
