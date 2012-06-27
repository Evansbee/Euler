prev1 = 1
term = 2
sum = 2

while term < 4000000:
   newterm = term + prev1
   prev1 = term
   term = newterm

   if term % 2 == 0:
      sum += term

print sum
