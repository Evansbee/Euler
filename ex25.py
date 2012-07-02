f1, f2 = 1,1

term = 2
while len(str(f2)) < 1000:
   f1 , f2, term = f2, f1+f2, term + 1

print term
