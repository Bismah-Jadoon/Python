# Write a program to input name, marks and phone number of a student and format it using the format function like below:
# "The name of the student is Harry, his marks are 72 and phone number is 99999888"

name = input("Enter your name: ")
marks = int(input("Enter your marks: "))
phone = int(input("Enter your phone number: "))

# format function
a = "The name of the student is {}, marks are {} and phone number is {}".format(name,marks,phone)

print(a)

