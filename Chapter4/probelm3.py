# Show that tuple cannot change in python

a = ("hello", 1, 2.3, False)
print(a[0])

a[0] = "hi"
print(a) #it will give error