#python program to check armstrong number without the remainder ,using list comprehension

#input here
n = input("Enter a number :")
s = 0

# for i in n:
#     s += int(i)**len(n)
s = [(int(i)**len(n)) for i in n]

if ( sum(s) == int(n) ):
    print("Number is Armstrong")
else:  
    print("Number is not Armstrong")    
