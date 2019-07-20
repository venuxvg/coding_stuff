# Product of even places is exactly divisible by sum of odd places

inp1 = int(input('Enter a number: '))
nd = 1
s = 0
p = 1

while(inp1>0):
    r = inp1 % 10
    if (nd % 2 == 0):
        p = p * r
    else:
        s = s + r
    inp1 = inp1 // 10
    nd += 1

if ( p % s == 0):
    print('True')
else:
    print('False')