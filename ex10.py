from EvEuler import ListOfPrimesUnder

answer = 0

primes = ListOfPrimesUnder(2000001)

for i in primes:
	answer = answer + i

print answer
