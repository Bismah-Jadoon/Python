#  A span comment is defines as a text containing following keywords:
#  "make a lot of money", "buy now", "subscribe this", "click this".Write a program to detect these spams

p1 = "make a lot of money"
p2 = "buy now"
p3 = "subscribe this" 
p4 = "click this"

message = input("Enter your comment: ")

if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("This message is a spam ")

else:
    print("This message is not a spam")