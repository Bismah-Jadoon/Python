# write a program to find greatest of four numbers entered by the user

number1 = int(input("Enter number 1: "))
number2 = int(input("Enter number 2: "))
number3 = int(input("Enter number 3: "))
number4 = int(input("Enter number 4: "))

if(number1 > number2 and number1 > number3 and number1 > number4):
    print(number1, "is greater ")

elif(number2 > number1 and number2 > number3 and number2 > number4):
   print(number2, "is greater")

elif(number3 > number1 and number3 > number2 and number4):
   print(number3, "is greater")

else:
   print("All are equal")