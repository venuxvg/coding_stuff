# Python program to make a simple Calculator
def calcu(choice):
        switcher={
                1: print(f'Addition of {inp1} and {inp2}:{inp1+inp2}'),
                2: print(f'Subtraction of {inp1} and {inp2}:{inp1-inp2}'),
                3: print(f'Multiplication of {inp1} and {inp2}:{inp1*inp2}'),
                4: print(f'Division of {inp1} and {inp2}:{inp1/inp2}'),
             }
        #print(switcher.get(choice,'Please read the title and enter values correctly'))

print('Please Enter two values')
inp1 = int(input('Value of A:'))
inp2 = int(input('Value of B:'))
print('Simple Calculator \n1.Addition \n2.Subtraction \n3.Multiplication \n4.Division')
choice = input('Select one option:')
calcu(choice)


# switch (choice):
# case 1 : 
    
#     break
# case 2 :
#     
#     break
# case 3 :
#     
#     break
# case 4 :
#     
#     break
# default :
#     
#     break
