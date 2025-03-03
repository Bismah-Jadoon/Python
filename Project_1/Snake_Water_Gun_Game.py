'''
Snake vs. Water: Snake drinks the water hence wins.
Water vs. Gun: The gun will drown in water, hence a point for water
Gun vs. Snake: Gun will kill the snake and win.
'''

import random


# Function for computer to choose a random string
def computer():
    list = ["Snake", "Water", "Gun"]
    choice = random.choice(list)
    return choice
    

# Function for Human to choose between Snake, Water, Gun
def Human():
    choice = input("Enter your choice : ")
    return choice


# Function call and allocating it to variables 
a = computer()
b = Human()


# Just to make it clear for the user about the choice of Computer and Human we print the choices
print(f"Computer choose : {a}")
print(f"Human choose : {b}")


# if statements for conditions
if(a == b):
        print("Match Withdraw")
elif(a == "Snake" and b == "Water"):
         print("Computer Wins!! Snake drinks the water hence wins")
elif(a == "Water" and b == "Gun"):
         print("Computer Wins!! The gun will drown in water, hence a point for water")
elif(a == "Gun" and b == "Snake"):
         print("Computer Wins!! Gun will kill the snake and win")
elif(b == "Snake" and a == "Water"):
         print("Human Wins!! Snake drinks the water hence wins")
elif(b == "Water" and a == "Gun"):
         print("Human Wins!! The gun will drown in water, hence a point for water")
elif(b == "Gun" and a == "Snake"):
         print("Human Wins!! Gun will kill the snake and win")
     
