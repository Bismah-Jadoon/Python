# 1
# a = (1, 2, 3, 5, 4) #we use close brackets so it is tuple, tuples are immutable 
# print(type(a)) #return <class 'tuple'>

# 2
#  if we want to print tuple with only 1 element then
# a = (1)
# print(type(a)) # it will return int because it is not tuple with one element

# 3
# correct method
# a = (1,) # you have to put "," after that 1 element to make it tuple
# print(type(a))

# 4
#  empty tuple
a = ()
print(type(a))

# 5
# tuple can be of different datatypes 
a = ("hello", 1, 4.2, False, "Shine")
print(type(a))

# we cannot change an element of tuple like lists
a[0] = "one" 

