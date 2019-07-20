# python program to print second biggest number among three numbers by tarun

a = int(input('Enter first value: '))
b = int(input('Enter second value: '))
c = int(input('Enter third value: '))

if ( a > b and b > c):
    a = 0
else:
    if( b > c ):
        b = 0
    else:
        c = 0

if ( a > b and a > c ):
    print(f'{a} is the second biggest number')
else:
    if( b > c ):
        print(f'{b} is the second biggest number')
    else:
        print(f'{c} is the second biggest number')
