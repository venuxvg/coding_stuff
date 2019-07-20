# Python program to make a simple Calculator
def calcu(choice,inp1,inp2):
        switcher={
                '1': f'Addition of {inp1} and {inp2}:{inp1+inp2}',
                '2': f'Subtraction of {inp1} and {inp2}:{inp1-inp2}',
                '3': f'Multiplication of {inp1} and {inp2}:{inp1*inp2}',
                '4': f'Division of {inp1} and {inp2}:{inp1/inp2}'
        }
        if(choice in switcher):
                print(switcher[choice])
        else:
                print("Please read the title and enter values correctly")       

print('Please Enter two values')
inp1 = int(input('Value of A:'))
inp2 = int(input('Value of B:'))
print('Simple Calculator \n1.Addition \n2.Subtraction \n3.Multiplication \n4.Division')
choice = input('Select one option:')
calcu(choice,inp1,inp2) 