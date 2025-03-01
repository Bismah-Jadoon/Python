# Loops in Python

Loops in Python are used to execute a block of code repeatedly. Python provides two primary types of loops: `for` and `while` loops. These loops help automate repetitive tasks, making code more efficient and readable.

---

## 1. The `for` Loop

The `for` loop is used to iterate over a sequence (such as a list, tuple, dictionary, string, or range object). It executes a block of code for each item in the sequence.

### Syntax:
```python
for variable in sequence:
    # Code to execute
```

### Example:
```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```
#### Output:
```
apple
banana
cherry
```

### Using `range()` in `for` Loop
The `range()` function generates a sequence of numbers that can be used to control the number of iterations.

```python
for i in range(5):
    print(i)
```
#### Output:
```
0
1
2
3
4
```

---

## 2. The `while` Loop

The `while` loop executes a block of code as long as a given condition is `True`.

### Syntax:
```python
while condition:
    # Code to execute
```

### Example:
```python
count = 0
while count < 5:
    print(count)
    count += 1
```
#### Output:
```
0
1
2
3
4
```

---

## 3. Loop Control Statements
Python provides several statements to control loop execution:

### a) `break` Statement
The `break` statement exits the loop prematurely when a condition is met.

```python
for num in range(10):
    if num == 5:
        break
    print(num)
```
#### Output:
```
0
1
2
3
4
```

### b) `continue` Statement
The `continue` statement skips the current iteration and moves to the next one.

```python
for num in range(5):
    if num == 2:
        continue
    print(num)
```
#### Output:
```
0
1
3
4
```

### c) `else` Clause in Loops
An `else` block in a loop runs when the loop terminates normally (without a `break` statement).

```python
for i in range(3):
    print(i)
else:
    print("Loop completed")
```
#### Output:
```
0
1
2
Loop completed
```

---

## 4. Nested Loops
A loop inside another loop is called a nested loop.

### Example:
```python
for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")
```
#### Output:
```
i=0, j=0
i=0, j=1
i=1, j=0
i=1, j=1
i=2, j=0
i=2, j=1
```

---

## 5. Infinite Loops
If the loop condition never becomes `False`, the loop runs indefinitely.

### Example:
```python
while True:
    print("This is an infinite loop")
    break  # Breaking the loop to prevent infinite execution
```

---

## 6. Iterating Over Different Data Structures
Python loops can iterate over various data structures.

### a) Iterating Over a String
```python
for char in "Python":
    print(char)
```

### b) Iterating Over a Dictionary
```python
data = {"name": "Alice", "age": 25}
for key, value in data.items():
    print(f"{key}: {value}")
```

### c) Iterating Over a Set
```python
colors = {"red", "green", "blue"}
for color in colors:
    print(color)
```

---

## Conclusion
Loops are a fundamental concept in Python that help automate repetitive tasks. The `for` loop is ideal for iterating over sequences, while the `while` loop is useful when the number of iterations is unknown. Loop control statements like `break`, `continue`, and `else` provide finer control over loop execution. Understanding these concepts enables efficient and effective coding in Python.


