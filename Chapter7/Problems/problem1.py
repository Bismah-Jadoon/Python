#  write a program to print multiplication table using for loop

n = int(input("Enter your number: "))

for i in range(1, 11):
    print(f"{n} X {i} = {n * i}")