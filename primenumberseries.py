# python program to find prime numbers in  a sequence

# start = int(input()) # if needed
# end = int(input())  # if needed
start = 1
end = 101
for num in range(start,end):
    if(num > 1):
        for i in range(2,(num//2)+1):
            if (num % i) == 0:
                break
        else:
            print(num)