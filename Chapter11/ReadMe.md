# Inheritance in Python

## Introduction
Inheritance is one of the core principles of object-oriented programming (OOP). It allows one class (child or derived class) to inherit the attributes and methods of another class (parent or base class). This promotes code reusability and hierarchical relationships between classes.

## Types of Inheritance in Python
Python supports multiple types of inheritance:
1. **Single Inheritance**
2. **Multiple Inheritance**
3. **Multilevel Inheritance**
4. **Hierarchical Inheritance**
5. **Hybrid Inheritance**

---

## 1. Single Inheritance
A child class inherits from one parent class.

```python
class Parent:
    def parent_method(self):
        return "This is a method from the Parent class"

class Child(Parent):
    def child_method(self):
        return "This is a method from the Child class"

obj = Child()
print(obj.parent_method())  # Output: This is a method from the Parent class
print(obj.child_method())   # Output: This is a method from the Child class
```

---

## 2. Multiple Inheritance
A child class inherits from multiple parent classes.

```python
class Parent1:
    def method1(self):
        return "Method from Parent1"

class Parent2:
    def method2(self):
        return "Method from Parent2"

class Child(Parent1, Parent2):
    def child_method(self):
        return "Method from Child"

obj = Child()
print(obj.method1())  # Output: Method from Parent1
print(obj.method2())  # Output: Method from Parent2
print(obj.child_method())  # Output: Method from Child
```

---

## 3. Multilevel Inheritance
A class is derived from another derived class, forming a chain.

```python
class Grandparent:
    def grandparent_method(self):
        return "Method from Grandparent"

class Parent(Grandparent):
    def parent_method(self):
        return "Method from Parent"

class Child(Parent):
    def child_method(self):
        return "Method from Child"

obj = Child()
print(obj.grandparent_method())  # Output: Method from Grandparent
print(obj.parent_method())       # Output: Method from Parent
print(obj.child_method())        # Output: Method from Child
```

---

## 4. Hierarchical Inheritance
One parent class is inherited by multiple child classes.

```python
class Parent:
    def parent_method(self):
        return "Method from Parent"

class Child1(Parent):
    def child1_method(self):
        return "Method from Child1"

class Child2(Parent):
    def child2_method(self):
        return "Method from Child2"

obj1 = Child1()
obj2 = Child2()
print(obj1.parent_method())  # Output: Method from Parent
print(obj2.parent_method())  # Output: Method from Parent
```

---

## 5. Hybrid Inheritance
A combination of two or more types of inheritance.

```python
class Base:
    def base_method(self):
        return "Method from Base"

class Parent1(Base):
    def parent1_method(self):
        return "Method from Parent1"

class Parent2(Base):
    def parent2_method(self):
        return "Method from Parent2"

class Child(Parent1, Parent2):
    def child_method(self):
        return "Method from Child"

obj = Child()
print(obj.base_method())   # Output: Method from Base
print(obj.parent1_method())  # Output: Method from Parent1
print(obj.parent2_method())  # Output: Method from Parent2
print(obj.child_method())    # Output: Method from Child
```

---

## Method Resolution Order (MRO)
MRO determines the sequence in which methods are inherited in case of multiple inheritance. Python follows the **C3 Linearization (Depth-First Left-to-Right)** method.

To check MRO, use:
```python
print(Child.__mro__)
```
or
```python
help(Child)
```

---

## Overriding Methods
A child class can override a parent class method.

```python
class Parent:
    def show(self):
        return "Parent Class Method"

class Child(Parent):
    def show(self):
        return "Child Class Method"

obj = Child()
print(obj.show())  # Output: Child Class Method
```

---

## Using `super()` to Access Parent Methods
The `super()` function allows you to call a method from the parent class.

```python
class Parent:
    def show(self):
        return "Parent Class Method"

class Child(Parent):
    def show(self):
        return super().show() + " (Modified by Child)"

obj = Child()
print(obj.show())  # Output: Parent Class Method (Modified by Child)
```

---

# The `@property` Decorator in Python

## Introduction
The `@property` decorator in Python is used to define **getter, setter, and deleter methods** for managing attribute access in an object-oriented way. It allows controlled access to private attributes while maintaining a clean and readable syntax.

## Basic Usage of `@property`
A **property** allows a method to be accessed like an attribute. This is useful when you want to enforce some logic while retrieving a value.

```python
class Person:
    def __init__(self, name):
        self._name = name  # Private attribute convention (_name)
    
    @property
    def name(self):
        """Getter method for name."""
        return self._name

person = Person("Alice")
print(person.name)  # Output: Alice
```

## Using `@property` with a Setter
A **setter** allows modification of a private attribute while enforcing constraints.

```python
class Person:
    def __init__(self, name):
        self._name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string!")
        self._name = value

person = Person("Alice")
person.name = "Bob"  # Allowed
print(person.name)  # Output: Bob
```

Trying to set a non-string value will raise an error:

```python
person.name = 123  # Raises ValueError: Name must be a string!
```

## Using `@property` with a Deleter
A **deleter** method allows controlled deletion of an attribute.

```python
class Person:
    def __init__(self, name):
        self._name = name
    
    @property
    def name(self):
        return self._name
    
    @name.deleter
    def name(self):
        print("Deleting name...")
        del self._name

person = Person("Alice")
del person.name  # Output: Deleting name...
```

## Full Example with Getter, Setter, and Deleter
```python
class Employee:
    def __init__(self, salary):
        self._salary = salary
    
    @property
    def salary(self):
        """Getter for salary."""
        return self._salary
    
    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Salary cannot be negative!")
        self._salary = value
    
    @salary.deleter
    def salary(self):
        print("Deleting salary...")
        del self._salary

emp = Employee(5000)
print(emp.salary)  # Output: 5000
emp.salary = 6000  # Update salary
print(emp.salary)  # Output: 6000
del emp.salary     # Deletes salary
```

## Advantages of `@property`
- **Encapsulation**: Restricts direct access to private attributes.
- **Readability**: Allows accessing methods like attributes (`obj.attribute` instead of `obj.attribute()`).
- **Validation**: Allows logic enforcement (e.g., preventing negative values in setters).

## Conclusion 1
The `@property` decorator in Python is a powerful tool for managing attribute access while maintaining clean, readable code. By using getter, setter, and deleter methods, we can add logic to attribute access while keeping it intuitive.


## Conclusion 2
Inheritance is a powerful feature in Python that helps in creating reusable and modular code. Understanding its different types and techniques like method overriding and MRO allows for more efficient and scalable applications.


