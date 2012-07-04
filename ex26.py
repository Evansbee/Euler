
def GetInvFactors(num):
   remainders = [1]
   answer = []

   while remainders[-1] and remainders[-1] != 0:
      answer.append(int(remainders[-1]/num))
      new_rem = (remainders[-1] - answer[-1] * num) * 10 
      if remainders.count(new_rem)>0:
         return answer,remainders.index(new_rem)+1
      if answer[-1] == 0:
         remainders[-1] = remainders[-1] * 10
      else:
         remainders.append(new_rem)

   return answer, None




repeats,repeatnum = 0,0
seq = []
for d in range(1,1001):
   factors,repeat = GetInvFactors(d)
   if repeat != None:
      if (len(factors)-repeat) > repeats:
         repeats,repeatnum = len(factors)-repeat,d

print "%d has %d repeating digits." %(repeatnum,repeats)
