# python program to print the array elements in ascending order

inp = int(input('How many elements you want to enter:'))
arr = []
for i in range(inp):
    n = input()
    arr.append(int(n))
arr.sort()
print(arr)
