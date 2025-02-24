#  create an empty dictionary. Allow 4 friends to enter their fav language as values and use keys as their names. Assume that the names are unique
d = {}

# 1st friend
name = input("Enter your name: ")
language = input("Enter your favorite language: ")
d.update({name:language})

# 2nd friend
name = input("Enter your name: ")
language = input("Enter your favorite language: ")
d.update({name:language})

# 3rd friend
name = input("Enter your name: ")
language = input("Enter your favorite language: ")
d.update({name:language})

# 4th friend
name = input("Enter your name: ")
language = input("Enter your favorite language: ")
d.update({name:language})

print(d) # key can be same but values in a dictionary can not be same
