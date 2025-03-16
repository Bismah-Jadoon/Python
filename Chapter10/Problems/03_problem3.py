# Create a class with a class attribute a; create an object from it and set 'a' directly using object.a = world. Does this change the class attribute?
# No, class attribute doesn't change but an instance attribute is set
class employee:
    a = "Hello"

obj = employee()
obj.a = "World"
print(obj.a)