ans = []

for d in range(2,999999):
   val = 0
   for i in range(len(str(d))):
      val += int(str(d)[i])**5
   if d == val:
      ans.append(d)

answer = 0
for i in ans:
   answer += i
print ans
print "-------------------"
print answer
