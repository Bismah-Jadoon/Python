class Employee:
    a = 1
    def __init__(self):
        print("I am constructor of Employee class")

class Programmer(Employee):
    b = 2
    def __init__(self):
        print("I am constructor of Programmer class")

class Manager(Programmer):
    c = 3
    
    def __init__(self):
        super().__init__() #run constructor of parent class as well
        print("I am constructor of Manager class")


o = Manager()
print(o.a, o.b, o.c)