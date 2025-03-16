class operator:
    
    def __init__(self,n):
        self.n = n

    def __add__(self, num):
        return self.n + num.n 
    
    def __truediv__(self, num):
        return self.n / num.n 
    
    def __floordiv__(self, num):
        return self.n / num.n
    
       
n = operator(1)
m = operator(2)

print(n + m)
print(n / m)
print(n // m)
