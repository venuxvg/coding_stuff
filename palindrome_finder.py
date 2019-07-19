# write a program to find the all palindromes in the range 70 to 700

m = int(input('Enter a number:'))
n = int(input("Enter a number:"))

if(m > 999 or n > 999):
    print("I will only take atmost 3 digit number")
    exit()
if(m > n):
    print("Please read the program title")

# for storing numbers sequence
listo = []

# for storing the values from the list
a = [] 
 
for i in range(m,n+1,1):
    listo.append(i)

for i in range(len(listo)):
    a = 0
    a = [int(j) for j in str(listo[i])]
    if(a[0] == a[-1]):
        if(len(a) == 2):
            print(f'Given number {listo[i]} is not a palindrome')
        else:
            print(f'Given number {listo[i]} is palindrome')
    else:
        print(f'Given number {listo[i]} is not a palindrome')
