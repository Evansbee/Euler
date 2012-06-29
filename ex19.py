#days per month (non leap)
dpm = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

#day of week for when i start counting
dow = 1

#dictionary by (day, month, year) => day of week, 0 is sunday
cal = {}

for y in range(1900,2001):
   for m in range(1,13): #fucking non-inclusive range function
      days = dpm[m]
      
      #leapy
      if y % 4 == 0:
         days += 1

      
      for d in range(1, dpm[m]+1):
         cal[(d,m,y)] = dow
         dow = (dow + 1) % 7


counter = 0

#i went back and made days 1 based too, anal!
for y in range(1901,2001):
   for m in range(1,13):
      if cal[(1,m,y)] == 0:
         counter += 1

print counter
