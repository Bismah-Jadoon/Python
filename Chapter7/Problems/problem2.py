# write a program to greet all person names stored in a list l1 and which starts with S
l1 = ["Harry", "Shubham", "Sachin", "Rahul"]

for name in l1:
    if(name.startswith("S")):
        print(f"Hello {name}")