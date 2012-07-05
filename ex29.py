ans = []

for a in range(2,101):
   for b in range(2,101):
      ans.append(a**b)

ans = set(ans)
print len(ans)
