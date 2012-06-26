sequences = []

longest = 0
num = 0
for i in range(1,1000000):
   current = [i]
   print i
   while current[-1] != 1:
      if current[-1] % 2 == 0:
         current.append(current[-1]/2)
      else:
         current.append(3*current[-1] + 1)

   if len(current) > longest:
      longest = len(current)
      num = i

   #sequences.append(current)



print num
   

