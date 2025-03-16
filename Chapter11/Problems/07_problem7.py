# override the __len__() method on vector of problem 5 to display the dimension of the vector

#  Write a class vector representing a vector of n dimensions. Overload the + and * operator which calculates the sum and the dot(.) product of them.

class Vector:
    def __init__(self,l):
        self.l = l

    def __len__(self):
        return len(self.l)
    
    
v1 = Vector([1, 2, 3])
print(len(v1))


