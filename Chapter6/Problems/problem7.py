# Write a program to find out whether a post is talking about "Harry" or not

p1 = "Hi! How are you, Harry"
# name = "harry"
name = "Harry"

if(name.lower() in p1.lower()): #it will convert the upper case to lower both for post and name then it'll check
    print("Yes the post is talking about 'Harry' ")
else:
    print("NO the post is not talking about 'Harry' ")