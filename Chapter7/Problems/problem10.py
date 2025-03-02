# Write a program to print a multiplication table of n using for loop in reversed order

n = int(input("Enter a number: "))
i = 10
for i in range(1, 11):
    print(f"{n} X {11 - i} = {n * (11 - i)}")