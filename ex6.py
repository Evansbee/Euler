sumofsquares = 0
squareofsums = 0

for i in range(1,101):
   sumofsquares = sumofsquares + (i * i)
   squareofsums = squareofsums + i
squareofsums = squareofsums * squareofsums
answer = squareofsums - sumofsquares

print answer
