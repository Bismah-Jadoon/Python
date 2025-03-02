# Python Documentation

## Introduction
Python is a high-level, interpreted programming language known for its simplicity and readability. It supports multiple programming paradigms, including procedural, object-oriented, and functional programming. Python is widely used for web development, data science, artificial intelligence, automation, scripting, scientific computing, and more.

## Features of Python
- **Easy to Learn and Use**: Python has a simple syntax similar to English, making it beginner-friendly.
- **Interpreted Language**: Python executes code line by line, allowing for quick debugging and testing.
- **Dynamically Typed**: Variables do not require explicit declaration of their data types.
- **Cross-Platform Compatibility**: Python programs can run on Windows, macOS, Linux, and other operating systems without modification.
- **Extensive Libraries**: Python has a vast standard library, including modules for file handling, networking, regular expressions, and databases.
- **Object-Oriented**: Supports encapsulation, inheritance, and polymorphism for modular programming.
- **High-Level Language**: Python abstracts complex low-level operations, improving productivity.
- **Garbage Collection**: Python has an automatic memory management system.

## Installation
Python can be downloaded from [python.org](https://www.python.org/). 
To check if Python is installed, use the command:
```sh
python --version
```
To install packages, use pip:
```sh
pip install package_name
```
To upgrade pip:
```sh
pip install --upgrade pip
```

## Basic Syntax
### Hello World
```python
print("Hello, World!")
```

### Variables and Data Types
```python
x = 10           # Integer
y = 3.14        # Float
name = "Alice"  # String
is_valid = True # Boolean
z = None        # NoneType
```

### Type Checking
```python
print(type(x))  # Output: <class 'int'>
print(type(y))  # Output: <class 'float'>
```

### Comments
```python
# This is a single-line comment
"""
This is a multi-line comment
or docstring.
"""
```

## Control Flow
### Conditional Statements
```python
x = 10
if x > 0:
    print("Positive number")
elif x == 0:
    print("Zero")
else:
    print("Negative number")
```

### Loops
#### For Loop
```python
for i in range(5):
    print(i)
```

#### While Loop
```python
x = 0
while x < 5:
    print(x)
    x += 1
```

#### Loop Control Statements
```python
for i in range(10):
    if i == 5:
        break  # Terminates the loop
    if i == 3:
        continue  # Skips the rest of the code for this iteration
    print(i)
```

## Functions
```python
def greet(name):
    return "Hello, " + name

print(greet("Alice"))
```

### Lambda Functions
```python
add = lambda a, b: a + b
print(add(3, 5))  # Output: 8
```

## Data Structures
### Lists
```python
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits[1])  # Output: banana
```

### Tuples (Immutable Lists)
```python
tuple_example = (1, 2, 3)
print(tuple_example[0])
```

### Sets (Unordered, Unique Elements)
```python
set_example = {1, 2, 3, 3}
print(set_example)  # Output: {1, 2, 3}
```

### Dictionaries (Key-Value Pairs)
```python
person = {"name": "Alice", "age": 25}
print(person["name"])  # Output: Alice
```

## Object-Oriented Programming (OOP)
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        return f"Hello, my name is {self.name}"

p1 = Person("Alice", 25)
print(p1.greet())
```

### Inheritance
```python
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
```

## File Handling
```python
# Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, World!")

# Reading from a file
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
```

## Exception Handling
```python
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("Execution completed.")
```

## Modules and Libraries
### Importing Modules
```python
import math
print(math.sqrt(16))  # Output: 4.0
```

### Popular Libraries
- **NumPy**: Numerical computations
- **Pandas**: Data manipulation
- **Matplotlib**: Data visualization
- **Requests**: Handling HTTP requests
- **TensorFlow**: Machine learning
- **Scikit-Learn**: Machine learning tools
- **Flask/Django**: Web development frameworks

## Virtual Environments
To create a virtual environment:
```sh
python -m venv myenv
```
To activate:
```sh
source myenv/bin/activate  # On macOS/Linux
myenv\Scripts\activate    # On Windows
```
To deactivate:
```sh
deactivate
```

## Advanced Topics
### List Comprehensions
```python
squares = [x ** 2 for x in range(10)]
print(squares)
```

### Generators
```python
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1
```

### Multithreading
```python
import threading

def print_numbers():
    for i in range(5):
        print(i)

thread = threading.Thread(target=print_numbers)
thread.start()
thread.join()
```

## Conclusion
Python is a powerful, versatile programming language with applications in various domains. Its ease of use, rich ecosystem, and vast community support make it an excellent choice for beginners and experts alike.

