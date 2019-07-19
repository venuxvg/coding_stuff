import numpy as np
arr = []
dim1 = int(input('Enter the first dimension scale:'))
dim2 = int(input('Enter the second dimension scale:'))
dim3 = int(input('Enter the third dimension scale:'))
sum = 0
arr = np.zeros((dim1,dim2,dim3))
for k in range(dim3):
    for i in range(dim1):
        for j in range(dim2):
            arr[i][j][k]= int(input('Enter a value:'))
    for i in range(dim1):
        for j in range(dim2):
            sum += arr[i][j][k]
print(sum)