# Python program to print the count Even Number  and  Even Sum  And Odd Number. 
# Sum and Odd Count between 1 to 100 numbers.

n = int(input("Enter number range :))
even = [i for i in range(0,n,2)]
odd = [i for i in range(1,n,2)]
print(f"Sum of Even Numbers is : {sum(even)}")
print(f"Sum of Odd Numbers is : {sum(odd)}")
