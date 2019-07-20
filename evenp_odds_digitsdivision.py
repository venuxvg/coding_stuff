# Product of even digits is exactly divisible by sum of odd digits

inp1 = int(input('Enter a number: '))
s = 0
p = 1
while(inp1>0):
    r = inp1 % 10
    if (r % 2 == 0):
        p = p * r
    else:
        s = s + r
    inp1 = inp1 // 10

if ( p % s == 0):
    print('True')
else:
    print('False')