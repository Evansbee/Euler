def RowCorners(rw):
   if rw==1:
      return [1]
   
   le = rw**2

   ur = le
   ul = le - (rw-1)
   ll = ul - (rw-1)
   lr = ll - (rw-1)


   return [ur,ul,ll,lr]

total = 0
for i in range(1,1002,2):
   for diag in RowCorners(i):
      total += diag
print total
