# Classes and Objects in Python

## Introduction
In Python, a class is a blueprint for creating objects. An object is an instance of a class that contains data (attributes) and behavior (methods). Python follows an object-oriented programming (OOP) paradigm that enables code reusability and modularity.

## Defining a Class
A class is defined using the `class` keyword.

```python
class MyClass:
    """A simple example class."""
    def __init__(self, name, age):
        self.name = name  # Attribute
        self.age = age    # Attribute
    
    def greet(self):
        """Method to print a greeting message."""
        return f"Hello, my name is {self.name} and I am {self.age} years old."
```

## Creating Objects
Objects are instances of a class and are created using the class name followed by parentheses.

```python
person1 = MyClass("Alice", 25)
print(person1.greet())  # Output: Hello, my name is Alice and I am 25 years old.
```

## Class Attributes vs Instance Attributes
- **Instance Attributes**: Defined inside the `__init__` method and unique to each instance.
- **Class Attributes**: Shared among all instances of a class.

```python
class Example:
    class_attr = "I am a class attribute"
    
    def __init__(self, value):
        self.instance_attr = value
```

## Special Methods (Magic Methods)
Python provides built-in special methods (also called magic or dunder methods) that allow customization of class behavior.

### `__init__`: Constructor Method
Called when an instance is created.

```python
def __init__(self, param1, param2):
    self.param1 = param1
    self.param2 = param2
```

### `__str__`: String Representation
Defines a user-friendly string representation of an object.

```python
def __str__(self):
    return f"Object with param1: {self.param1}, param2: {self.param2}"
```

### `__repr__`: Developer-Friendly Representation
Used to generate a representation of the object.

```python
def __repr__(self):
    return f"ClassName({self.param1}, {self.param2})"
```

### `__del__`: Destructor
Called when an object is deleted.

```python
def __del__(self):
    print(f"Object {self.param1} is being deleted")
```

## Instance Methods, Class Methods, and Static Methods
Python supports different types of methods inside a class.

### Instance Methods
Operate on instance attributes and require `self`.

```python
def instance_method(self):
    return f"This is an instance method."
```

### Class Methods
Operate on class attributes and use `@classmethod`.

```python
class MyClass:
    class_variable = "Class Level Data"
    
    @classmethod
    def class_method(cls):
        return f"Accessing {cls.class_variable} from class method"
```

### Static Methods
Do not modify class or instance attributes and use `@staticmethod`.

```python
class MyClass:
    @staticmethod
    def static_method():
        return "This is a static method."
```

## Inheritance
Inheritance allows a class to inherit attributes and methods from another class.

```python
class Parent:
    def parent_method(self):
        return "This is a method from the Parent class"

class Child(Parent):
    def child_method(self):
        return "This is a method from the Child class"
```

## Method Overriding
A child class can override a method of the parent class.

```python
class Parent:
    def show(self):
        return "Parent Class"

class Child(Parent):
    def show(self):
        return "Child Class"
```

## Encapsulation
Encapsulation is restricting direct access to variables and methods by using private (`__`), protected (`_`), and public attributes.

```python
class Example:
    def __init__(self):
        self.public = "I am public"
        self._protected = "I am protected"
        self.__private = "I am private"
```

## Polymorphism
Polymorphism allows objects of different classes to be treated as objects of a common superclass.

```python
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Bark"

class Cat(Animal):
    def speak(self):
        return "Meow"
```

## Conclusion
Python’s class and object system provides powerful object-oriented programming capabilities, including encapsulation, inheritance, and polymorphism. Understanding these concepts enables better code organization and reusability.


