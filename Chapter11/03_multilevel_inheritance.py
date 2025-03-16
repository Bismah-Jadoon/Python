class Employee:
    a = 1

class Programmer(Employee):
    b = 2

class Manager(Programmer):
    c = 3

o = Employee()
print(o.a) #it will print 1 bcz it is the Employee class attribute
# print(o.b) #it will give an error bcz b is not the Employee class attribute

o = Programmer()
print(o.a, o.b)

o = Manager()
print(o.a, o.b, o.c)