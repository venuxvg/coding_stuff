# python program to print second biggest number among three numbers

a = int(input('Enter first value: '))
b = int(input('Enter second value: '))
c = int(input('Enter third value: '))

if( (a > b) and (a > c)):
    if ( b > c ):
        print(f'{b} is the second biggest digit')
    else:
        print(f'{c} is the second biggest digit')
else:
    if ( b > c ):
        if ( a > c ):
            print(f'{a} is the second biggest digit')
        else:
            print(f'{c} is the second biggest digit')
    else:
        if ( a > b):
            print(f'{a} is the second biggest digit')
        else:
            print(f'{b} is the second biggest digit')