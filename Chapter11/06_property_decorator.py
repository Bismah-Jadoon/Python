class Employee:
    a = 1

    @classmethod 
    def show(cls):
        print(f"The value is {cls.a}")

    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter
    def name(self,value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]


o = Employee()
o.name = "Harry Potter"
print(o.fname, o.lname)


