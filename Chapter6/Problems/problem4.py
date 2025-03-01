# Write a program to find whether a given username contains less than 10 characters or not
name = input("Enter your name : ")
length = len(name)

print("Your name length is : ", length)
if(length < 10):
    print("Your name character is less than 10")
elif(length == 10):
    print("Your name character is equal to 10")
else:
    print("Your name character is greater than 10")