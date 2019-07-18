#python program to check armstrong number for n numbers using commandline arguments

import sys
Armstrong_with_commandline = sys.argv[0]  
num = int(sys.argv[1]) 
sum = 0  
num1 = num  
listo = [int(i) for i in str(num)]
powa = len(listo)
print(powa)
  
while num1 > 0:  
   i = num1 % 10  
   sum += i ** powa
   num1 //= 10  
  
if num == sum:  
   print(num,"is an Armstrong number")  
else:  
   print(num,"is not an Armstrong number")