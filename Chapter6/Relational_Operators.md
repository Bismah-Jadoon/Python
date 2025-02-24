
---

# **Complete Documentation on Conditional Expressions and Relational Operators in Python**

## **1. Introduction**
Conditional expressions and relational operators are fundamental to decision-making in Python. They allow programs to evaluate conditions and execute specific code based on whether conditions are **True** or **False**.

### **Topics Covered:**
1. **Relational Operators** (Comparison operators)
2. **Conditional Expressions**
3. **Usage in `if`, `if-else`, and loops**
4. **Best Practices and Common Mistakes**

---

# **2. Relational Operators**
Relational operators, also called **comparison operators**, are used to compare values and return a Boolean result (`True` or `False`).

## **2.1 List of Relational Operators**
Python provides six relational operators:

| Operator | Name | Description | Example |
|----------|------|-------------|---------|
| `==` | Equal to | Checks if two values are equal | `5 == 5 → True` |
| `!=` | Not equal to | Checks if two values are not equal | `5 != 3 → True` |
| `>` | Greater than | Checks if left operand is greater than the right | `10 > 5 → True` |
| `<` | Less than | Checks if left operand is smaller than the right | `2 < 8 → True` |
| `>=` | Greater than or equal to | Checks if left operand is greater than or equal to the right | `5 >= 5 → True` |
| `<=` | Less than or equal to | Checks if left operand is smaller than or equal to the right | `4 <= 7 → True` |

### **2.2 Examples of Relational Operators**
#### **Equality (`==`) and Inequality (`!=`)**
```python
a = 10
b = 20

print(a == b)   # False (10 is not equal to 20)
print(a != b)   # True  (10 is not equal to 20)
```

#### **Greater Than (`>`) and Less Than (`<`)**
```python
x = 15
y = 10

print(x > y)  # True (15 is greater than 10)
print(x < y)  # False (15 is not less than 10)
```

#### **Greater Than or Equal To (`>=`) and Less Than or Equal To (`<=`)**
```python
age = 18

print(age >= 18)  # True (18 is equal to 18)
print(age <= 21)  # True (18 is less than or equal to 21)
```

---

## **3. Conditional Expressions**
Conditional expressions allow Python to execute different code blocks based on conditions.

### **3.1 `if` Statement**
Executes a block of code if a condition is **True**.

#### **Syntax:**
```python
if condition:
    statement(s)
```
#### **Example:**
```python
age = 18
if age >= 18:
    print("You are eligible to vote.")
```

---

### **3.2 `if-else` Statement**
Executes one block if a condition is **True**, otherwise executes another block.

#### **Syntax:**
```python
if condition:
    statement(s)  # Executes if condition is True
else:
    statement(s)  # Executes if condition is False
```

#### **Example:**
```python
num = 10
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")
```

---

### **3.3 `if-elif-else` Statement**
Checks multiple conditions **sequentially**.

#### **Syntax:**
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

#### **Example:**
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

---

### **3.4 Ternary Conditional Expression (One-Line `if-else`)**
Python provides a **compact way** to write simple conditional statements.

#### **Syntax:**
```python
value_if_true if condition else value_if_false
```

#### **Example:**
```python
age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)  # Output: Adult
```

---

### **3.5 Using Relational Operators in Conditional Statements**
#### **Example: Checking if a Number is Positive**
```python
num = 5

if num > 0:
    print("Positive number")
else:
    print("Not a positive number")
```

#### **Example: Checking Voting Eligibility**
```python
age = 17

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")
```

---

## **4. Using Relational Operators and Conditionals in Loops**
Relational operators are often used in loops to control execution.

#### **Example: Counting from 1 to 5**
```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

---

## **5. Chaining Relational Operators**
Python allows **chaining** of relational operators for cleaner comparisons.

#### **Example: Checking if a Number is Between Two Values**
```python
num = 15

if 10 <= num <= 20:
    print("Number is between 10 and 20")
else:
    print("Number is outside the range")
```

---

## **6. Common Mistakes and Best Practices**
### **6.1 `=` vs. `==` (Assignment vs. Comparison)**
```python
x = 10  # Assignment
if x == 10:  # Comparison
    print("x is 10")
```
🚨 **Mistake:** Using `=` instead of `==` in conditions:
```python
if x = 10:  # ❌ SyntaxError
    print("Incorrect usage")
```

---

### **6.2 Comparing Different Data Types**
Python allows comparisons between numbers but not between incompatible types.
```python
print(5 > 3.5)  # ✅ True (int vs float is valid)
print("5" > 3)  # ❌ TypeError (string vs int)
```

---

## **7. Summary Table**
### **Relational Operators**
| Operator | Meaning | Example | Output |
|----------|---------|---------|--------|
| `==` | Equal to | `5 == 5` | `True` |
| `!=` | Not equal to | `5 != 3` | `True` |
| `>` | Greater than | `10 > 5` | `True` |
| `<` | Less than | `2 < 8` | `True` |
| `>=` | Greater than or equal to | `5 >= 5` | `True` |
| `<=` | Less than or equal to | `4 <= 7` | `True` |

### **Conditional Expressions**
| Statement Type | Usage |
|---------------|-------|
| `if` | Executes code if condition is `True` |
| `if-else` | Provides an alternative when condition is `False` |
| `if-elif-else` | Handles multiple conditions |
| Ternary Expression | One-line `if-else` |

---

## **8. Conclusion**
- **Relational operators** compare values and return `True` or `False`.
- **Conditional expressions** use relational operators to make decisions in programs.
- Used in **`if` statements, loops, and Boolean logic**.
- Be cautious of **type mismatches** and **`=` vs. `==` mistakes**.

