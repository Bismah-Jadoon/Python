class Employee:
    name = "Harry"
    language = "Py" #this is class attribute
    salary  = 1200000

obj = Employee()
obj.language = "JS" #this is instance attribute 
print(obj.language, obj.salary)

# the instance attribute takes priority over class attribute and will print JS