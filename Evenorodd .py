# Python program to find given number is even or odd

inp = int(input("Enter a number to check wheather its even or odd :"))

if( inp % 2 == 0):
    print(f'Given {inp} is even')
else:
    print(f'Given {inp} is odd')