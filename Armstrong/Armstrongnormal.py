#python program to check armstrong number ,normal method.

#input here
num = int(input("Enter a number: "))  
sum = 0  
num1 = num 
  
while num1 > 0:  
   i = num1 % 10  
   sum += i ** 3  
   num1 //= 10  
  
if num == sum:  
   print(num,"is an Armstrong number")  
else:  
   print(num,"is not an Armstrong number")
