try:
    num = int(input("Enter a number : "))
    print(num)

except Exception as e:
    print(e)

else:
    print("I am inside else") #this will work when try is successful