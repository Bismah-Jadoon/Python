def greet(name, ending):
    print("Good day! " + name)
    print(ending)

greet("Shine", "Thank You")


def greet(name, ending):
    print("Good day! " + name)
    print(ending)

a = greet("Shine", "Thank You")
print(a) # a give a none value 

# to solve this we use return function , the return function return a value to any variable that was called
# return is a value of a function and if u give that value to any variable , it's value was then given to that variable

def greet(name, ending):
    print("Good day! " + name)
    print(ending)
    return "done"

a = greet("Shine", "Thank You")
print(a) 