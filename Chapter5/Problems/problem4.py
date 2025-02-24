# what will be the length of the following program:
s = set()
s.add(20)
s.add(20.0) 
s.add("20")

print(len(s)) #it return 2 bcz 20 == 20.0 in python , in python datatype does not matter if both values are numerically equal