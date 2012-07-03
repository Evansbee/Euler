from decimal import Decimal

seq = []
for d in range(1,1001):
   seq.append(Decimal(1.0)/Decimal(d))
   print seq[-1]


