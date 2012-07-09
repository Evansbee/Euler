def IsPalindrome(word):
   for i in range(0,len(word)/2):
      if word[i] != word[-1-i]:
         return False
   return True

palindromes = []
for i in range(1,1000000):
   if IsPalindrome(str(i)) and IsPalindrome('{:b}'.format(i)):
      palindromes.append(i)

ans = 0
for i in palindromes:
   ans += i
print ans
