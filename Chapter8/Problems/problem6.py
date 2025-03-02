# write a program using function which converts inches to cms

# formula => cm = inches * 2.54

def conversion():
    inches = int(input("Enter vlaue in inches: "))
    return inches * 2.54

print(f"The corresponding value in cms is : {conversion()}")