# Functions and Recursion in Python

## 1. Functions in Python

### 1.1 Introduction
Functions in Python are reusable blocks of code that perform a specific task. Functions help in modular programming by breaking a program into smaller and manageable parts.

### 1.2 Defining a Function
A function is defined using the `def` keyword, followed by the function name and parentheses containing optional parameters.

#### Syntax:
```python
def function_name(parameters):
    """Docstring explaining the function"""
    # Function body
    return value  # Optional
```

#### Example:
```python
def greet(name):
    """This function greets the user by name."""
    return f"Hello, {name}!"

print(greet("Alice"))
```

### 1.3 Calling a Function
A function is called using its name followed by parentheses containing arguments if required.
```python
result = greet("Bob")
print(result)
```

### 1.4 Function Arguments
Python functions can take different types of arguments:
1. **Positional Arguments**: Arguments passed in the correct order.
2. **Keyword Arguments**: Arguments identified by parameter names.
3. **Default Arguments**: Arguments with default values.
4. **Variable-Length Arguments**: `*args` for multiple positional arguments, `**kwargs` for multiple keyword arguments.

#### Example:
```python
def add(a, b=5):
    return a + b

print(add(3))       # Uses default b=5
print(add(3, 7))    # Overrides default
```

### 1.5 Return Statement
Functions can return values using the `return` statement.
```python
def square(n):
    return n * n

print(square(4))
```

### 1.6 Anonymous (Lambda) Functions
Lambda functions are single-expression functions defined using the `lambda` keyword.
```python
square = lambda x: x * x
print(square(5))
```

## 2. Recursion in Python

### 2.1 What is Recursion?
Recursion is a technique where a function calls itself to solve a smaller subproblem of the original problem.

### 2.2 Base Case and Recursive Case
A recursive function must have:
1. **Base Case**: Condition that stops recursion.
2. **Recursive Case**: Function calls itself with a modified argument.

#### Example: Factorial Function
```python
def factorial(n):
    if n == 0 or n == 1:  # Base Case
        return 1
    return n * factorial(n - 1)  # Recursive Case

print(factorial(5))  # Output: 120
```

### 2.3 Recursive vs Iterative Approach
Some problems can be solved both iteratively and recursively. Recursion is more elegant but can lead to high memory usage due to multiple function calls.

#### Example: Fibonacci Series
Recursive approach:
```python
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))  # Output: 8
```

Iterative approach:
```python
def fibonacci_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

print(fibonacci_iterative(6))  # Output: 8
```

### 2.4 Advantages and Disadvantages of Recursion
**Advantages:**
- Simplifies code for problems like tree traversal, factorial, Fibonacci, etc.
- Provides a clear and logical approach to certain algorithms.

**Disadvantages:**
- Higher memory consumption due to multiple function calls.
- Risk of stack overflow if recursion depth is too high.
- Slower execution compared to iterative solutions in some cases.

### 2.5 Tail Recursion
Tail recursion is an optimized form of recursion where the recursive call is the last operation in the function. Python does not optimize tail recursion by default.

#### Example:
```python
def tail_recursive_factorial(n, acc=1):
    if n == 0:
        return acc
    return tail_recursive_factorial(n - 1, n * acc)

print(tail_recursive_factorial(5))  # Output: 120
```

## 3. Conclusion
Functions and recursion are fundamental concepts in Python that help in code reusability and problem-solving. While recursion simplifies certain problems, it should be used judiciously to avoid excessive memory usage and performance issues.


