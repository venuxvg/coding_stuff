# Python program to find the sum of the digits of given number

inp=input("Enter a number :") 
a = [ int(i) for i in inp ]
print(f'The sum of digits of given number : {sum(a)}')