class Employee:
    name = "Harry"
    language = "Py"
    salary  = 1200000

    def getInfo(self): # it will give error when we dont use self method here 
        print(f"The language is {self.language}.The salary is {self.salary}")

    def __init__(self,name,language, salary): #__init__ is called dunder method in python which is automatically called
        self.name = name
        self.language = language
        self.salary = salary
        print("I am creating an object")
         
    
    @staticmethod #we are defining this method as static method
    def greet(): # if we dont want to give self method then we make that method static
        print("Good morning")

obj = Employee("Shine", "JS", 130000) # dunder method is called
print(obj.name, obj.salary, obj.language)

