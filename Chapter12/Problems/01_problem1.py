# Write a program to open three files 1.txt, 2.txt and 3.txt if any these files are not present, a message without exiting the program must be printed prompting the same.
with open("one.txt", "r") as f1, open("two.txt", "r") as f2, open("three.txt", "r") as f3:
    content1 = f1.read()
    content2 = f2.read()
    content3 = f3.read()

print(content1,content2,content3)