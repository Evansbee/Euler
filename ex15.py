values = {}

MAX = 21

for x in range(MAX):
   for y in range (MAX):
      values[(x,y)]=0


for i in range (MAX):
   values[(MAX-1,i)]=1
   values[(i,MAX-1)]=1

for x in range(MAX-2,-1,-1):
   for y in range(MAX-2,-1,-1):
      values[(x,y)] = values[(x+1,y)] + values[(x,y+1)]
      print "Updating (%d, %d)" % (x,y)

print values[0,0]
      
