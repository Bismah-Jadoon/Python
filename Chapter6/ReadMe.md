# **Complete Documentation on Conditional Expressions in Python**

## **1. Introduction**
Conditional expressions in Python allow for decision-making by evaluating conditions and executing code accordingly. They help control the flow of execution in programs based on logic.

Python provides multiple ways to express conditions:
- **if statements**
- **if-elif-else chains**
- **Ternary conditional expressions**
- **Short-circuit evaluation**
- **Pattern matching (Python 3.10+)**

---

## **2. The `if` Statement**
The `if` statement allows executing a block of code **only if** a condition is `True`.

### **Syntax:**
```python
if condition:
    statement(s)
```

### **Example:**
```python
age = 18
if age >= 18:
    print("You are eligible to vote.")
```
### **Explanation:**
- If `age` is 18 or more, the `print` statement executes.
- If `age` is less than 18, nothing happens.

---

## **3. The `if-else` Statement**
The `if-else` statement provides an **alternative block of code** to execute if the condition is `False`.

### **Syntax:**
```python
if condition:
    statement(s)  # Executes if condition is True
else:
    statement(s)  # Executes if condition is False
```

### **Example:**
```python
num = 10
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")
```

### **Explanation:**
- If `num` is divisible by 2, **"Even number"** prints.
- Otherwise, **"Odd number"** prints.

---

## **4. The `if-elif-else` Statement**
The `if-elif-else` statement is used when multiple conditions need to be checked **sequentially**.

### **Syntax:**
```python
if condition1:
    statement(s)
elif condition2:
    statement(s)
elif condition3:
    statement(s)
else:
    statement(s)  # Executes if none of the above conditions are True
```

### **Example:**
```python
marks = 85

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Grade: F")
```

### **Explanation:**
- If `marks` is 90 or more, "Grade: A" prints.
- If `marks` is between 75 and 89, "Grade: B" prints.
- If `marks` is between 50 and 74, "Grade: C" prints.
- Otherwise, "Grade: F" prints.

---

## **5. Ternary Conditional Expression (One-Line `if-else`)**
Python provides a **compact way** to write simple conditional statements using **ternary conditional expressions**.

### **Syntax:**
```python
value_if_true if condition else value_if_false
```

### **Example:**
```python
age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)  # Output: Adult
```

### **Explanation:**
- If `age >= 18`, `status` is `"Adult"`.
- Otherwise, `status` is `"Minor"`.

This is equivalent to:
```python
if age >= 18:
    status = "Adult"
else:
    status = "Minor"
```
The ternary expression **improves readability** for simple cases.

---

## **6. Short-Circuit Evaluation in Conditionals**
Python uses **short-circuiting** to optimize boolean expressions. This means that Python **stops evaluating** as soon as the result is determined.

### **Example with `and`:**
```python
x = 10
y = 0
if y != 0 and x / y > 2:  # Avoids division by zero
    print("Result is greater than 2")
else:
    print("Condition is False")
```
- Since `y != 0` is `False`, Python **does not evaluate** `x / y > 2`, avoiding a division error.

### **Example with `or`:**
```python
name = None
default_name = name or "Guest"
print(default_name)  # Output: Guest
```
- Since `name` is `None` (which is falsy), Python assigns `"Guest"`.

---

## **7. Using `in` and `not in` in Conditionals**
Python provides `in` and `not in` to check membership in lists, tuples, sets, or strings.

### **Example:**
```python
fruits = ["apple", "banana", "cherry"]

if "banana" in fruits:
    print("Banana is available.")
```

### **Example with `not in`:**
```python
banned_users = ["user1", "user2"]
username = "user3"

if username not in banned_users:
    print("Access granted.")
```

---

## **8. Using Boolean Operators (`and`, `or`, `not`)**
Python provides logical operators to combine multiple conditions.

| Operator | Description |
|----------|------------|
| `and`    | Returns `True` if **both** conditions are `True` |
| `or`     | Returns `True` if **at least one** condition is `True` |
| `not`    | Negates the condition |

### **Example:**
```python
age = 25
has_license = True

if age >= 18 and has_license:
    print("You can drive.")
```

---

## **9. The `match` Statement (Pattern Matching, Python 3.10+)**
Python 3.10 introduced **pattern matching** using `match-case` statements.

### **Syntax:**
```python
match variable:
    case pattern1:
        statement(s)
    case pattern2:
        statement(s)
    case _:
        statement(s)  # Default case (like else)
```

### **Example:**
```python
status_code = 404

match status_code:
    case 200:
        print("OK")
    case 404:
        print("Not Found")
    case 500:
        print("Server Error")
    case _:
        print("Unknown Status")
```

---

## **10. Nesting Conditional Statements**
You can nest `if` statements within other `if` statements.

### **Example:**
```python
num = 15

if num > 0:
    if num % 2 == 0:
        print("Positive Even Number")
    else:
        print("Positive Odd Number")
else:
    print("Not a positive number")
```

---

## **11. Best Practices for Writing Conditionals**
✅ **Use ternary expressions** for simple conditions:
```python
status = "Active" if is_logged_in else "Inactive"
```

✅ **Use short-circuiting** to prevent unnecessary operations:
```python
if user and user.is_admin:
    print("Admin Access")
```

✅ **Avoid deeply nested `if` statements**; use `elif`:
```python
if condition1:
    ...
elif condition2:
    ...
```

✅ **Use `match-case`** for multiple specific values (Python 3.10+).

✅ **Use `in` for membership checks** instead of multiple `or` conditions:
```python
if fruit in ["apple", "banana", "cherry"]:
    ...
```

---

## **12. Summary Table**
| Statement Type | Usage |
|---------------|-------|
| `if` | Executes code if condition is `True` |
| `if-else` | Provides an alternative when condition is `False` |
| `if-elif-else` | Handles multiple conditions |
| Ternary Expression | One-line `if-else` |
| `match-case` | Pattern matching (Python 3.10+) |
| `and`, `or`, `not` | Logical operations in conditions |

---

## **13. Conclusion**
Python's conditional expressions provide flexibility for controlling program flow. Understanding `if`, `if-else`, `if-elif-else`, ternary expressions, and short-circuiting helps write efficient, readable code.



