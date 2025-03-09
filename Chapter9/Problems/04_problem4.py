#  A file contains a word "Donkey" multiple times. You need to write a program which replaces this word with ###### by updating the same file..

word = "Donkey"

with open("problem4file.txt","r") as f:
    content = f.read()

newContent = content.replace(word, "######")

with open("problem4file.txt","w") as f:
    f.write(newContent)