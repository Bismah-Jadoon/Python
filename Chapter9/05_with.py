# f = open("file.txt")
# print(f.read())
# f.close()

# The same thing can happen using with statement u dont have to close the file explicitly

with open("file.txt") as f:
    print(f.read())