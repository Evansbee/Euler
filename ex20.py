from math import factorial

fact = str(factorial(100))

count = 0
for i in range(len(fact)):
   count += int(fact[i])

print count
