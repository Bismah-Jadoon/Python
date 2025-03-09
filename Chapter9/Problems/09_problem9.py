# Write a program to find out whether a file is identical & matches the Content another file.

with open("file1.txt","r") as f:
    content1 = f.read()

with open("file2.txt", "r") as f:
    content2 = f.read()

if(content1 == content2):
    print("Yes, the content of file1 and file2 is same")
else:
    print("No, the content of file1 and file2 is not same")