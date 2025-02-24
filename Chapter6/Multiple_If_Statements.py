age = int(input("Enter your age : "))

# If statement no: 1
if(age%2 == 0):
    print("age is even")

# End of If statement no: 1

# If statement no: 2
if(age >= 18):
    print("You are above the age of consent")
    print("Good for you")

elif(age < 0):
    print("You are entering an invalid negative age")

elif(age == 0):
    print("You are entering 0")

else:
    print("You are below the age of consent")
# End of If statement no: 2

print("End program")