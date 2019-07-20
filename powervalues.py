# Power of given value

x = int(input('Enter value for base: '))
y = int(input('Enter value for power: '))
sums = 1

for i in range(y):
    sums = sums*x

print(f'Power of {x} and {y}: {sums}')

sums1 = sums
n = 0
while(sums > 0):
    r = sums % 10
    n+=1
    sums = sums // 10
print(f'Number of digits in {sums1}: {n}')