words = ["Donkey", "bad"]

with open("problem5file.txt", "r") as f:
    content = f.read()

    for word in words:
       content = content.replace(word, "#" * len(word))

with open("problem5file.txt", "w") as f:
    f.write(content)