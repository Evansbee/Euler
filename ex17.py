numbers = { 0:"", 1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",\
            10:"ten",11:"eleven",12:"twelve",13:"thirteen", 14:"fourteen",15:"fifteen",16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen",\
            20:"twenty",30:"thirty",40:"fourty",50:"fifty",60:"sixty",70:"seventy",80:"eighty",90:"ninty",\
            100:"onehundred", 200:"twohundred",300:"threehundred",400:"fourhundred",500:"fivehundred",600:"sixhundred",700:"sevenhundred",\
            800:"eighthundred", 900:"ninehundred", 1000:"onethousand"}



def needsthousands(num):
   return num >= 1000 and num 

def needshundreds(num):
   return num % 1000 >= 100 and num % 1000 != 0

def needstens(num):
   return num % 100 >= 10 and num % 100 != 0

def needsones(num):
   return num >= 1 and num % 10 != 0 and (num % 100 < 10 or num % 100 > 19)

def needsand(num):
   return needshundreds(num) and (needstens(num) or needsones(num))

def getthousands(num):
   if needsthousands(num):
      return (num / 1000) * 1000
   return 0

def gethundreds(num):
   if needshundreds(num):
      return (num / 100) * 100
   return 0

def gettens(num):
   if needstens(num):
      num = num % 100
      if num > 10 and num < 20:
         return num
      return (num / 10) * 10
   return 0

def getones(num):
   if needsones(num):
      return num % 10
   return 0

def numstring(num):
   pass

count = 0 

for i in range(1000):
   num = i+1
   cn = ""
   cn += numbers[getthousands(num)]
   cn += numbers[gethundreds(num)]
   if needsand(num):
      cn += "and"
   cn += numbers[gettens(num)]
   cn += numbers[getones(num)]
   count += len(cn)
   print "%d = %s" % ( num , cn ) 
   
print count   
