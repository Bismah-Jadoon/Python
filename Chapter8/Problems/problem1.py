# write a program using function to find greatest of three numbers

def greatest(a,b,c):
    if(a > b and a>c):
        return a
    elif(b > a and b>c):
        return b
    elif(c > b and c>a):
        return c
   
    
a = 1
b = 23
c = 24
print(greatest(a, b, c))
