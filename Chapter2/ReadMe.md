# Python Variables, Data Types, Operators, and Input Function

## 1. Variables in Python
A **variable** in Python is a name that refers to a value stored in memory. You can assign values to variables using the `=` operator. Variables do not require explicit declaration; they are dynamically typed.

### Example:
```python
x = 10  # Integer variable
y = 3.14  # Floating-point variable
name = "Alice"  # String variable
is_valid = True  # Boolean variable
```

### Characteristics of Variables:
- Python is **dynamically typed**, meaning variables do not require explicit type declarations.
- A variable’s type is determined at runtime based on the assigned value.
- Variables are **case-sensitive** (`age` and `Age` are different variables).

## 2. Data Types in Python
Python supports various data types, including:

- **Numeric Types**
  - `int` (Integer): Whole numbers (e.g., `10`, `-3`, `100`)
  - `float` (Floating-point): Decimal numbers (e.g., `3.14`, `-0.99`)
  - `complex`: Complex numbers (e.g., `3+4j`)
- **Boolean Type**
  - `bool`: Represents `True` or `False`
- **Sequence Types**
  - `str`: String (e.g., "Hello")
  - `list`: Ordered collection (e.g., `[1, 2, 3]`)
  - `tuple`: Immutable ordered collection (e.g., `(4, 5, 6)`)  
- **Set Types**
  - `set`: Unordered unique collection (e.g., `{1, 2, 3}`)
- **Mapping Type**
  - `dict`: Key-value pairs (e.g., `{"name": "Alice", "age": 25}`)

### Checking Data Types
You can use the `type()` function to check the data type of a variable:
```python
x = 10
y = 3.14
print(type(x))  # Output: <class 'int'>
print(type(y))  # Output: <class 'float'>
```

## 3. Rules for Defining Variable Names in Python
When naming variables, follow these rules:

- Variable names **must start** with a letter (a-z, A-Z) or an underscore (`_`).
- The rest of the name can contain letters, digits (0-9), and underscores.
- Variable names **cannot be** a Python keyword (e.g., `if`, `while`, `import`, `def`).
- Python is **case-sensitive**, so `Age` and `age` are different.
- Use descriptive names for better readability.

### Valid Variable Names:
```python
my_var = 10
_myVar = 20
myVar123 = 30
```

### Invalid Variable Names:
```python
2var = 5  # Invalid: Cannot start with a number
my-var = 10  # Invalid: Cannot use hyphens
class = "Python"  # Invalid: 'class' is a reserved keyword
```

## 4. Type Casting in Python
Type casting is the process of converting one data type to another. Python provides built-in functions for explicit type conversion.

### Common Type Casting Functions:
- `int()`: Converts a value to an integer.
- `float()`: Converts a value to a floating-point number.
- `str()`: Converts a value to a string.
- `bool()`: Converts a value to a boolean.

### Example:
```python
x = "10"
y = "3.5"

# Convert string to integer and float
num1 = int(x)  # 10
num2 = float(y)  # 3.5

# Convert number to string
str_num = str(num1)  # "10"

# Convert number to boolean
bool_val = bool(num1)  # True (non-zero values are True)

print(num1, type(num1))  # Output: 10 <class 'int'>
print(num2, type(num2))  # Output: 3.5 <class 'float'>
print(str_num, type(str_num))  # Output: "10" <class 'str'>
print(bool_val, type(bool_val))  # Output: True <class 'bool'>
```

### Implicit Type Casting
Python sometimes converts data types automatically without explicit conversion.
```python
x = 5  # int
y = 2.5  # float
z = x + y  # Implicitly converts x to float
print(z, type(z))  # Output: 7.5 <class 'float'>
```

## 5. Operators in Python
Operators perform operations on variables and values. Python supports the following types of operators:

### 5.1 Arithmetic Operators
Used for mathematical operations:
```python
x = 10
y = 3
print(x + y)  # Addition (13)
print(x - y)  # Subtraction (7)
print(x * y)  # Multiplication (30)
print(x / y)  # Division (3.333...)
print(x // y)  # Floor Division (3)
print(x % y)  # Modulus (1)
print(x ** y)  # Exponentiation (1000)
```

### 5.2 Comparison Operators
Used for comparison between values:
```python
a = 5
b = 10
print(a == b)  # False
print(a != b)  # True
print(a > b)  # False
print(a < b)  # True
print(a >= b)  # False
print(a <= b)  # True
```

### 5.3 Logical Operators
Used to combine conditional statements:
```python
x = True
y = False
print(x and y)  # False
print(x or y)  # True
print(not x)  # False
```

#### Truth Table for Logical Operators
| A       | B       | A and B | A or B | not A |
|---------|---------|---------|--------|-------|
| True    | True    | True    | True   | False |
| True    | False   | False   | True   | False |
| False   | True    | False   | True   | True  |
| False   | False   | False   | False  | True  |

### 5.4 Assignment Operators
Used to assign values to variables:
```python
x = 5
x += 3  # x = x + 3 (8)
x -= 2  # x = x - 2 (6)
x *= 4  # x = x * 4 (24)
x /= 3  # x = x / 3 (8.0)
```

## 6. The `input()` Function in Python
The `input()` function allows users to take input from the keyboard. By default, it returns input as a string.

### Example:
```python
name = input("Enter your name: ")
print("Hello, " + name + "!")
```

### Converting Input to Other Data Types
```python
age = int(input("Enter your age: "))  # Converts input to integer
height = float(input("Enter your height: "))  # Converts input to float
```

### Using `input()` with Formatting
```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"Hello {name}, you are {age} years old.")
```

