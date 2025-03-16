# We are going to write a program that generates a random number and asks the user to guess it.
# If the player's guess is higher than the actual number, the program displays "Lower number please". Similarly, if the user's guess is too low, the program prints "higher number please" When the user guesses the correct number, the program displays the number of guesses the player used to arrive at the number.
# Hint: Use the random module.

from random import randint

n = randint(1,100)
guess = 0
a = -1
while(a != n):
   a = int(input("Guess the number between 1 and 100: "))
   if(a > n):
      print("Enter a lower number")
      guess += 1
   elif(a < n):
      print("Enter a higher number")
      guess += 1
   elif(a == n):
      print(f"You guess the correct number {n}")

print(f"Your guesses are : {guess}")    