# Python Strings - Complete Documentation

## 1. Introduction to Strings
A **string** in Python is a sequence of characters enclosed in **single (' ')**, **double (" ")**, or **triple quotes (''' ''' or """ """)**.

### Example:
```python
string1 = 'Hello'
string2 = "World"
string3 = '''Multiline 
String'''
```

## 2. String Immutability
Strings in Python are **immutable**, meaning once a string is created, it cannot be changed. Any modification to a string results in a new string being created.

### Example:
```python
s = "Hello"
s[0] = "J"  # This will raise a TypeError
```

To modify a string, you must create a new one:
```python
s = "Hello"
s = "J" + s[1:]
print(s)  # Output: Jello
```

## 3. String Indexing
- Python strings support **zero-based indexing**.
- Positive indexing starts from `0` (left to right).
- Negative indexing starts from `-1` (right to left).

### Example:
```python
s = "Python"
print(s[0])  # Output: P
print(s[-1]) # Output: n
```

## 4. String Slicing
- Syntax: `string[start:end:step]`
- Default values:
  - `start = 0`
  - `end = length of string`
  - `step = 1`

### Example:
```python
s = "Python"
print(s[0:4])  # Output: Pyth
print(s[:3])   # Output: Pyt
print(s[::2])  # Output: Pto
print(s[::-1]) # Output: nohtyP (Reversed String)
```

## 5. Escape Sequences
Escape sequences allow inserting special characters in a string.

| Escape Sequence | Meaning |
|----------------|---------|
| `\n` | New line |
| `\t` | Tab space |
| `\\` | Backslash |
| `\'` | Single quote |
| `\"` | Double quote |

### Example:
```python
print("Hello\nWorld")  # Output: Hello (new line) World
```

## 6. String Methods
Python provides numerous built-in functions to manipulate strings.

### 6.1 `len()` Function
Returns the length of a string.
```python
s = "Python"
print(len(s))  # Output: 6
```

### 6.2 `isspace()` Function
Checks if a string contains **only whitespace characters**.
```python
print("   ".isspace())  # Output: True
print("Hello".isspace())  # Output: False
```

### 6.3 `find()` Function
Finds the **first occurrence** of a substring. Returns `-1` if not found.
```python
s = "Hello World"
print(s.find("World"))  # Output: 6
print(s.find("Python")) # Output: -1 (Not found)
```

### 6.4 Other String Functions

| Function | Description | Example |
|----------|-------------|---------|
| `upper()` | Converts string to uppercase | `'hello'.upper()  # 'HELLO'` |
| `lower()` | Converts string to lowercase | `'HELLO'.lower()  # 'hello'` |
| `strip()` | Removes leading/trailing spaces | `' hello '.strip()  # 'hello'` |
| `replace()` | Replaces substring with another | `'Hello'.replace('H', 'J')  # 'Jello'` |
| `split()` | Splits string into list | `'a,b,c'.split(',')  # ['a', 'b', 'c']` |
| `join()` | Joins list into string | `'-'.join(['a', 'b'])  # 'a-b'` |
| `capitalize()` | Capitalizes first letter | `'hello'.capitalize()  # 'Hello'` |
| `count()` | Counts occurrences of substring | `'hello'.count('l')  # 2` |
| `startswith()` | Checks if string starts with substring | `'Hello'.startswith('H')  # True` |
| `endswith()` | Checks if string ends with substring | `'Hello'.endswith('o')  # True` |

## 7. String Formatting
### Using `f-strings` (Python 3.6+)
```python
name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old.")
```

### Using `.format()`
```python
print("Hello, {}!".format("Alice"))  # Output: Hello, Alice!
```

## 8. Conclusion
Python strings are powerful, with many built-in methods for manipulation. Understanding these functions helps in effective text processing. Remember, **strings are immutable**, so modifying a string requires creating a new one.

---



