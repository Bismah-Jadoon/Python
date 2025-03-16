# write a class "calculator" capable of finding square, cube,and square root of a number

import math

class calculator:

    def __init__(self,n):
        self.n = n

    def square(self):
        print(f"The square of {self.n} is {self.n * self.n}")
    
    def cube(self):
        print(f"The cube of {self.n} is {self.n ** 3}")
    
    def sqroot(self):
        print(f"The square root of {self.n} is {self.n ** 1/2}")
        
    

obj = calculator(2)
obj.square()
obj.cube()
obj.sqroot()