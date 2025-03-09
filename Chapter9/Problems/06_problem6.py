# Write a program to mine a log file and find out whether it contains "python".


with open("log.html", "r") as f:
    content = f.read()
    
if("python" in content):
    print("This file contains the word python")
else:
    print("This file does not contain the word python")

