f = open("file.txt")

# lines = f.readlines() # this function give us the lines in our file in the form of list

# print(lines, type(lines)) 


# or by reaing line by line

# line1 = f.readline()
# print(line1, type(line1))

# line2 = f.readline()
# print(line2, type(line2))

# line3 = f.readline()
# print(line3, type(line3))

# line4 = f.readline()
# print(line4, type(line4))

# line5 = f.readline()
# print(line5 == "")



# using while loop

line = f.readline()

while(line != ""):
    print(line)
    line = f.readline()

f.close()

