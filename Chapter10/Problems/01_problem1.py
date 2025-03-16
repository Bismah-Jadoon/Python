# create a class "programmer" for storing info of few programmers working at microsoft

class Programmer:
     company = "Microsoft"
     
     def __init__(self,name,salary,language):
          self.name = name
          self.salary = salary
          self.language = language
          print(f"The employee {self.name} is working at {self.company}, {self.name} is expert in {self.language} language and earn {self.salary}.")

obj1 = Programmer("Shine", 120000,"Python")
# print(obj1.company,obj1.name,obj1.salary,obj1.language)
obj2 = Programmer("Harry", 130000,"JS")
# print(obj2.company,obj2.name,obj2.salary,obj2.language)
obj3 = Programmer("Pooh", 150000,"Java")
# print(obj3.company,obj3.name,obj3.salary,obj3.language)

