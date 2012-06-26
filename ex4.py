
def isPalindromic(number):
   forward = str(number)

   for i in range(0,len(forward)/2):
      if forward[i] != forward[len(forward)-1-i]:
         return False
   return True


large = 0

for i in range(100,999):
   for j in range(100,999):
      if isPalindromic(i * j) and i*j>large:
         large = i*j

   

print large
