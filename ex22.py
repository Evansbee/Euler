
names = []

for line in open('ex22.in','r'):
   for name in line.split(','):
      #stupid quotes...
      names.append(name[1:-1])

names.sort()

total = 0

for i in range(len(names)):
   word_score = 0
   for c in names[i]:
      word_score += (ord(c) - ord('A')) + 1
   score = word_score * (i+1)
   print "%s - w: %d p:%d"%(names[i],word_score,i+1)
   total += score

print score
