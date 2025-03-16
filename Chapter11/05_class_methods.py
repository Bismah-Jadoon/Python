class Employee:
    a = 1

    @classmethod #it is a class decorator and it is use to print class attributes instead of instance attributes
    def show(cls):
        print(f"The value is {cls.a}")


o = Employee()
o.a = 23 

o.show() #it will print 1 instead of 23 bcz we use @classmethod decorator which gives priority to class attribute