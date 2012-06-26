from math import *

for a in range(1,1001):
	for b in range(a,1001):
		c = sqrt((a**2) + (b**2))
		if a+b+c == 1000:
			print "a=%d, b=%d, c=%d, abc=%d"%(a,b,c,a*b*c)
			
	
