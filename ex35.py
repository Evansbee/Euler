from EvEuler import ListOfPrimesUnder

primes = ListOfPrimesUnder(1000000)

for i in primes[:]:
   if i < 10:
      continue


   if str(i).count('0') > 0:     
      primes.remove(i)
      continue
   if str(i).count('2') > 0:     
      primes.remove(i)
      continue
   if str(i).count('4') > 0:     
      primes.remove(i)
      continue
   if str(i).count('5') > 0:     
      primes.remove(i)
      continue
   if str(i).count('6') > 0:     
      primes.remove(i)
      continue
   
   if str(i).count('8') > 0:     
      primes.remove(i)
      continue

def NumRot(num,rot):
   ans = ""
  
   for i in range(rot,len(str(num))):
      ans += str(num)[i]

   for i in range(0,rot):
      ans += str(num)[i]

   return int(ans)

def Rotations(num):
   #will return a list of rotations
   #including the orig
   ans = []
   for i in range(len(str(num))):
      ans.append(NumRot(num,i)) 

   return ans

ans = []
i = 0

while i < len(primes):
   num = primes[i]
   rots = Rotations(num)
   fullRot = True
   for j in rots:
      if primes[primes.index(num):].count(j)>0:
         pass
      else:
         fullRot = False

   if fullRot:
      ans += rots
      print rots
   i += 1
print set(ans)
print len(set(ans))
