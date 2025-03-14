class Employee:
    name = "Harry"
    language = "Py"
    salary  = 1200000

    def getInfo(self): # it will give error when we dont use self method here 
        print(f"The language is {self.language}.The salary is {self.salary}")
    
    def greet(self): # self attribute is given to every function in class
        print("Good morning")

obj = Employee()
obj.getInfo() # this takes an argument it is same as => Employee.getInfo(obj) it takes obj as argument so we have to give self argument to the function
obj.greet()