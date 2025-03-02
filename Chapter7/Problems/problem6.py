# write a program to calculate the factorial of a given number using for loop
n = int(input("Enter a number: "))

fact = 1
for i in range(1, n + 1):
        if(n == 0):
          print("1")
        fact = fact * i
print(fact)

