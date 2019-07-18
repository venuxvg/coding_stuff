#python program to check armstrong number for n number of inputs

#input here
num = int(input("Enter a number: "))  
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