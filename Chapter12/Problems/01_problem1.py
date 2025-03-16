# Write a program to open three files 1.txt, 2.txt and 3.txt if any these files are not present, a message without exiting the program must be printed prompting the same.
try:
   with open("one.txt", "r") as f1: 
    content1 = f1.read()
except Exception as e:
  print(e)

try:
   with open("two.txt", "r") as f2:
    content2 = f2.read()
except Exception as e:
  print(e)

try:
   with open("three.txt", "r") as f3:
    content3 = f3.read()
except Exception as e:
  print(e)


