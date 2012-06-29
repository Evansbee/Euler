#just add it downward since we only need the answer, not every option
#challenge is the data structure -- let's try to read it in intelligently so I don't have to do something stupid in exercise 67

#file is in ex18.in

input = open("ex18.in", 'r')

row, col = 0 , 0

tri = {}


#well formated input means we can just dump this baby out
for line in input:
   for num in line.split():
      tri[(row,col)] = int(num)
      col += 1
   row += 1
   col = 0

for i in range(row-2, -1, -1):
   for j in range(i + 1):
      o1,o2 = tri[(i+1,j)], tri[(i+1,j+1)] 
      
      if o1 > o2:
         tri[(i,j)]+=o1
      else:
         tri[(i,j)]+=o2

print tri[(0,0)]
