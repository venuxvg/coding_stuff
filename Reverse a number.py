# Python Program to Reverse a Number

Num = int(input("Please Enter any Number: "))
Reverse = 0

while(Num > 0):
    Reminder = Num %10
    Reverse = (Reverse *10) + Reminder
    Num = Num //10

print(f"Reverse of entered number is = {Reverse}")