# **Complete Documentation on Dictionaries and Sets in Python**  

## **1. Dictionaries in Python**  
A **dictionary** in Python is an **unordered, mutable** collection that stores data in **key-value pairs**. It is defined using curly braces `{}` and allows fast lookups, additions, and deletions.

---

### **1.1 Creating a Dictionary**  
Dictionaries can be created using curly braces `{}` or the `dict()` function.

```python
# Creating a dictionary
my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# Using dict() constructor
dict_example = dict(name="Bob", age=30, city="Los Angeles")

print(my_dict)
print(dict_example)
```
**Output:**
```
{'name': 'Alice', 'age': 25, 'city': 'New York'}
{'name': 'Bob', 'age': 30, 'city': 'Los Angeles'}
```

---

### **1.2 Accessing Dictionary Elements**  
Access values using keys with `[]` or `get()`.

```python
print(my_dict["name"])  # Output: Alice
print(my_dict.get("age"))  # Output: 25
```

---

### **1.3 Modifying a Dictionary**  
Dictionaries are mutable; you can add, update, or remove key-value pairs.

```python
# Adding a new key-value pair
my_dict["gender"] = "Female"

# Updating a value
my_dict["age"] = 26

# Removing a key-value pair
del my_dict["city"]

print(my_dict)
```
**Output:**
```
{'name': 'Alice', 'age': 26, 'gender': 'Female'}
```

---

### **1.4 Dictionary Methods**  
| Method | Description | Example |
|--------|------------|---------|
| `keys()` | Returns all keys | `my_dict.keys()` |
| `values()` | Returns all values | `my_dict.values()` |
| `items()` | Returns key-value pairs as tuples | `my_dict.items()` |
| `get(key, default)` | Gets value for key, returns `default` if not found | `my_dict.get("age", 0)` |
| `update(dict2)` | Merges another dictionary | `my_dict.update({"age": 27})` |
| `pop(key)` | Removes and returns value for key | `my_dict.pop("age")` |
| `popitem()` | Removes and returns last key-value pair | `my_dict.popitem()` |
| `clear()` | Clears all items in the dictionary | `my_dict.clear()` |

---

### **1.5 Iterating Over a Dictionary**  

```python
for key in my_dict:
    print(key, my_dict[key])

for key, value in my_dict.items():
    print(f"{key}: {value}")
```

---

### **1.6 Dictionary Comprehension**  
Dictionary comprehensions allow creating dictionaries concisely.

```python
squares = {x: x**2 for x in range(1, 6)}
print(squares)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

---

### **1.7 Checking Membership (`in`, `not in`)**  
```python
print("name" in my_dict)  # Output: True
print("salary" not in my_dict)  # Output: True
```

---

### **1.8 Nested Dictionaries**  
Dictionaries can contain other dictionaries.

```python
nested_dict = {
    "student1": {"name": "Alice", "age": 25},
    "student2": {"name": "Bob", "age": 30}
}

print(nested_dict["student1"]["name"])  # Output: Alice
```

---

## **2. Sets in Python**  
A **set** is an **unordered, mutable** collection of unique elements. Sets do not allow duplicate values.

---

### **2.1 Creating a Set**  
Sets are created using curly braces `{}` or `set()`.

```python
# Creating a set
my_set = {1, 2, 3, 4, 5}

# Creating an empty set (must use set(), {} creates an empty dictionary)
empty_set = set()

print(my_set)
print(empty_set)
```

---

### **2.2 Accessing Set Elements**  
Sets do not support indexing or slicing because they are unordered.

---

### **2.3 Adding and Removing Elements**  
Use `add()`, `remove()`, and `discard()`.

```python
my_set.add(6)
my_set.remove(3)  # Removes 3 (raises an error if not found)
my_set.discard(10)  # No error if 10 is not in the set

print(my_set)
```

---

### **2.4 Set Operations**  
| Operation | Description | Example |
|-----------|------------|---------|
| `union(set2)` | Combines both sets (A ∪ B) | `A.union(B)` |
| `intersection(set2)` | Common elements (A ∩ B) | `A.intersection(B)` |
| `difference(set2)` | Elements in A, not in B (A - B) | `A.difference(B)` |
| `symmetric_difference(set2)` | Elements in A or B but not both (A ⊕ B) | `A.symmetric_difference(B)` |
| `issubset(set2)` | Checks if A ⊆ B | `A.issubset(B)` |
| `issuperset(set2)` | Checks if A ⊇ B | `A.issuperset(B)` |

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A | B)  # Union: {1, 2, 3, 4, 5, 6}
print(A & B)  # Intersection: {3, 4}
print(A - B)  # Difference: {1, 2}
print(A ^ B)  # Symmetric Difference: {1, 2, 5, 6}
```

---

### **2.5 Iterating Over a Set**  
```python
for item in my_set:
    print(item)
```

---

### **2.6 Set Comprehension**  
```python
squares = {x**2 for x in range(1, 6)}
print(squares)  # Output: {1, 4, 9, 16, 25}
```

---

### **2.7 Checking Membership (`in`, `not in`)**  
```python
print(3 in my_set)  # Output: True
print(10 not in my_set)  # Output: True
```

---

## **3. Differences Between Dictionaries and Sets**  

| Feature | Dictionary | Set |
|---------|-----------|-----|
| **Structure** | Key-value pairs | Unique unordered elements |
| **Mutability** | Mutable (keys are immutable) | Mutable |
| **Ordering** | Maintains insertion order (Python 3.7+) | Unordered |
| **Duplicates** | No duplicate keys | No duplicate values |
| **Operations** | `keys()`, `values()`, `items()` | Set operations (`union`, `intersection`, etc.) |
| **Accessing Elements** | By key | Cannot access by index |

---

### **Conclusion**
- **Dictionaries** store key-value pairs and allow fast lookups.
- **Sets** store unique, unordered elements and support mathematical operations.
- Both are **unordered collections**, but dictionaries maintain key-value relationships, while sets focus on uniqueness.

---
