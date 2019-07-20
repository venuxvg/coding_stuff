# Print the elements which are greater than the key element

a = []
print('Enter how many values you want to enter: ')
inp1 = int(input())

for i in range(inp1):
    ar = int(input())
    a.append(ar)

print('Enter key element :')
key = int(input())

for i in a:
    if(i > key**2):
        print(i)