from EvEuler import *
i = 2
triangle = 1
fin = False
while not fin:
   triangle = triangle + i
   if len(AllFactors(triangle)) > 500:
      print triangle
      fin = True
   i += 1
