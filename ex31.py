from EvEuler import irange
answer = 0
target = 200
for p200 in irange(target/200):
   for p100 in irange(target/100):
      for p50 in irange(target/50):
         for p20 in irange(target/20):
            for p10 in irange(target/10):
               for p5 in irange(target/5):
                  for p2 in irange(target/2):
                     val = 2*p2
                     val += 5*p5
                     val += 10*p10
                     val += 20*p20
                     val += 50*p50
                     val += 100*p100
                     val += 200*p200
                     if val <= target:
                        answer +=1
                        

print answer
