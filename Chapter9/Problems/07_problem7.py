# Write a program to find out the line number where python is present from Ques 6

with open("log.html") as f:
    lines = f.readlines()

lineno = 1
for line in lines:
    if("python" in line):
        print(f"python is in line : {lineno}")
        break
    lineno +=1
    
else:
    print("python is not present in the file")
