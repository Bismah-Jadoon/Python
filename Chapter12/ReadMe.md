

# 🐍 Advanced Python Concepts: A Complete Guide  

## 1️⃣ **Walrus Operator (`:=`)**  
The **Walrus operator** (`:=`), introduced in Python **3.8**, allows assignment within an expression.  

### ✅ **Why Use the Walrus Operator?**  
- Reduces redundant code.  
- Improves readability.  
- Helps in loops and conditions where we want to assign and check a value at the same time.  

### 📝 **Example 1: Without Walrus Operator**  
```python
value = input("Enter something: ")
if len(value) > 5:
    print("You entered more than 5 characters.")
```

### 🦦 **Example 2: With Walrus Operator**  
```python
if (value := input("Enter something: ")) and len(value) > 5:
    print("You entered more than 5 characters.")
```
This removes the need for a separate assignment statement.

---

## 2️⃣ **Type Definitions & Type Hints**  
Python is **dynamically typed**, meaning variables don't require explicit types. However, for clarity and better debugging, we can use **type hints**.

### ✅ **Basic Type Hints**
```python
def add_numbers(a: int, b: int) -> int:
    return a + b
```
- `a: int` → `a` should be an integer.  
- `b: int` → `b` should be an integer.  
- `-> int` → The function returns an integer.

### ✅ **Using `List`, `Tuple`, and `Dict`**  
```python
from typing import List, Tuple, Dict

def process_data(data: List[int]) -> Tuple[int, int]:
    return min(data), max(data)
```
- `List[int]` → A list containing integers.  
- `Tuple[int, int]` → Function returns a tuple of two integers.

---

## 3️⃣ **Advanced Type Hints**  
Python provides advanced type hints using `Union`, `Optional`, and more.

### ✅ **Union Type Hint (Multiple Possible Types)**  
```python
from typing import Union

def display(value: Union[int, str]):
    print(f"Value: {value}")
```
`Union[int, str]` means `value` can be either an `int` or `str`.

### ✅ **Optional Type Hint (Can be `None`)**  
```python
from typing import Optional

def greet(name: Optional[str] = None):
    if name:
        print(f"Hello, {name}!")
    else:
        print("Hello, Stranger!")
```
`Optional[str]` means the argument can be `str` or `None`.

---

## 4️⃣ **Match-Case (Pattern Matching)**  
Introduced in **Python 3.10**, `match-case` is Python’s version of `switch-case`.

### 📝 **Example:**
```python
def check_status(code: int):
    match code:
        case 200:
            print("Success")
        case 404:
            print("Not Found")
        case 500:
            print("Server Error")
        case _:
            print("Unknown Code")

check_status(200)  # Output: Success
```
`_` acts as the **default case**.

---

## 5️⃣ **Merge Dictionaries and Update**  
Python provides easy ways to **merge dictionaries**.

### ✅ **Using `|` Operator (Python 3.9+)**  
```python
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

merged_dict = dict1 | dict2
print(merged_dict)  # Output: {'a': 1, 'b': 3, 'c': 4}
```
- `|` merges two dictionaries.  
- If keys overlap, `dict2` values take precedence.

### ✅ **Using `.update()` Method**  
```python
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

dict1.update(dict2)
print(dict1)  # Output: {'a': 1, 'b': 3, 'c': 4}
```

---

## 6️⃣ **Multiple Context Managers (`with` Statement)**  
The `with` statement simplifies resource management.

### ✅ **Using Multiple Context Managers**
```python
with open("file1.txt") as f1, open("file2.txt") as f2:
    content1 = f1.read()
    content2 = f2.read()
```
- Opens **two files** at the same time.  
- Ensures both are closed properly.

---

## 7️⃣ **Exception Handling in Python**  
Python handles errors using `try-except`.

### ✅ **Basic Exception Handling**  
```python
try:
    num = int(input("Enter a number: "))
    print(10 / num)
except ValueError:
    print("Invalid input. Enter a number!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
```

---

## 8️⃣ **Raising Exceptions (`raise`)**  
You can manually trigger an error using `raise`.

```python
def check_age(age: int):
    if age < 18:
        raise ValueError("Age must be 18 or above!")
    print("Access Granted!")

check_age(15)  # Raises ValueError
```

---

## 9️⃣ **Try with Else Clause**  
- `else` executes if **no exception** occurs.

```python
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Invalid number!")
else:
    print("Valid number entered:", num)
```

---

## 🔟 **Try with Finally**  
- `finally` runs **no matter what** (even if an exception occurs).

```python
try:
    file = open("example.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found!")
finally:
    print("Closing file.")
    file.close()
```

---

## 1️⃣1️⃣ **`if __name__ == "__main__"`**  
This ensures that a script runs only when executed directly.

### ✅ **Example**  
```python
def greet():
    print("Hello, world!")

if __name__ == "__main__":
    greet()
```
If this script is **imported**, `greet()` won't run.

---

## 1️⃣2️⃣ **Global Variables in Python**  
A variable **outside a function** is global.

### ✅ **Example**  
```python
x = 10  # Global variable

def modify():
    global x
    x = 20  # Modifying global variable

modify()
print(x)  # Output: 20
```

---

## 1️⃣3️⃣ **`enumerate()` Function**  
Used to **loop with an index**.

### ✅ **Example**  
```python
fruits = ["Apple", "Banana", "Cherry"]
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)
```
Output:
```
1 Apple
2 Banana
3 Cherry
```

---

## 1️⃣4️⃣ **List Comprehension**  
A concise way to create lists.

### ✅ **Example:**
```python
squares = [x*x for x in range(1, 6)]
print(squares)  # Output: [1, 4, 9, 16, 25]
```

### ✅ **With Conditions**
```python
evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # Output: [0, 2, 4, 6, 8]
```

---

## 🎯 **Conclusion**  
These Python concepts improve **efficiency, readability, and error handling** in code. Understanding them makes you a **better Python developer**! 🚀🔥

