class Employee:
    company = "ITC"
    def show(self):
        print(f"The company is {self.company}")
class coder:
    language = "Python"
    def printLanguages(self):
       print(f"The language here is : {self.language}")
    
class Programmer(Employee, coder):
     company = "ITC InfoTech"
     name = "Shine"
     def showLanguage(self):
         print(f"The name is {self.name} and she is good with {self.language} language")

a = Employee()
b = Programmer()

b.show()
b.showLanguage()
b.printLanguages()