from math import sqrt

def irange(p1, p2=None, p3=1):
   if p2 == None:
      return range(0,p1+p3,p3)
   else:
      return range(p1,p2+p3,p3)

def AllFactors(number):
   allfactors = []
   topnumber = number
   if number == 1:
      return [1]
   i = 1 
   while i < topnumber:
      if number % i == 0:
         allfactors.append(i)
         allfactors.append(number/i)
         topnumber = number/i
      i = i + 1
   if allfactors.count(number) > 0:
      allfactors.remove(number)
   allfactors.sort()
   return list(set(allfactors))

#primefactors returns all prime factors such that
#multiplying all elements of the list together
#will result in the number
def PrimeFactors(number):
   primefactors = []
   i=2 
   while i < number:
      #is this number a factor of "number"
      if number % i == 0:
         #the ordering makes sure this is prime.
         primefactors.append(i)
         #we have a new top factor,  don't increase
         number = number / i
         if number == i:
            #toss another one on and break out
            # primefactors.append(i)
            break
      else:
         #not divisible so just break
         i = i+1
   #the last remaining number has to be prime
   primefactors.append(number)
   return primefactors


def IsPrime(num):
   if num < 1:
      return False
   factors = PrimeFactors(num)
   return len(factors) == 1 and factors[0] == num 

def ListOfPrimes(number):
   primelist = []
   return primelist
   
#def ListOfPrimesUnder(number):
#	primelist = []
#	i = 2
#	if number <= 2:
#		return []

#	while i < number:
#		div = False		
#		for j in primelist:
#			if i % j == 0:
#				div =True
#				break
#		if div == False:
#			print "added: %d" % i
#			primelist.append(i)
#		i = i + 1
#	return primelist


def ListOfPrimesUnder(number):
   primelist = range(2,number)
   i = 0
   while primelist[i] <= sqrt(number):
      currentval = primelist[i]
      if currentval != None:
         for j in range(i+currentval,len(primelist),currentval):
            primelist[j] = None
      i = i + 1
   realprimes = []
   for i in primelist:
      if i != None:
         realprimes.append(i)
   return realprimes


        
	
    








