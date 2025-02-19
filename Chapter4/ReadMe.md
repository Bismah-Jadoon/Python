Here’s a complete documentation of **Lists and Tuples in Python**, along with a comparison between **Strings and Lists**.  

---

# **Lists and Tuples in Python**

## **1. Lists in Python**
A **list** is a built-in data structure in Python that allows storing multiple items in a single variable. Lists are **mutable**, meaning their contents can be changed after creation.

### **1.1 Creating a List**
Lists are created using square brackets `[]` and can store multiple data types.
```python
# Creating a list
my_list = [1, 2, 3, 4, 5]
mixed_list = [1, "hello", 3.5, True]
```

### **1.2 Accessing List Elements**
Elements in a list can be accessed using indexing and slicing.
```python
# Indexing (starts from 0)
print(my_list[0])   # Output: 1

# Negative Indexing (starts from -1)
print(my_list[-1])  # Output: 5

# Slicing (start:stop:step)
print(my_list[1:4]) # Output: [2, 3, 4]
```

### **1.3 Modifying a List**
Lists allow modification after creation.
```python
# Changing an element
my_list[2] = 10  
print(my_list)  # Output: [1, 2, 10, 4, 5]

# Adding elements
my_list.append(6)  # Adds 6 to the end
print(my_list)     # Output: [1, 2, 10, 4, 5, 6]

# Removing elements
my_list.remove(10)  # Removes the first occurrence of 10
print(my_list)      # Output: [1, 2, 4, 5, 6]
```

### **1.4 List Methods**
| Method | Description | Example |
|--------|------------|---------|
| `append(x)` | Adds an element `x` to the end of the list | `list.append(10)` |
| `extend(iterable)` | Adds multiple elements from an iterable | `list.extend([10, 20])` |
| `insert(i, x)` | Inserts element `x` at index `i` | `list.insert(1, 5)` |
| `remove(x)` | Removes the first occurrence of `x` | `list.remove(5)` |
| `pop(i)` | Removes and returns the element at index `i` (default: last) | `list.pop(2)` |
| `index(x)` | Returns the index of first occurrence of `x` | `list.index(4)` |
| `count(x)` | Returns count of occurrences of `x` | `list.count(2)` |
| `sort()` | Sorts the list in ascending order | `list.sort()` |
| `reverse()` | Reverses the list | `list.reverse()` |
| `copy()` | Returns a copy of the list | `new_list = list.copy()` |

---

## **2. Tuples in Python**
A **tuple** is a collection of ordered elements like a list, but it is **immutable** (i.e., cannot be modified after creation).

### **2.1 Creating a Tuple**
Tuples are created using parentheses `()`.
```python
# Creating a tuple
my_tuple = (1, 2, 3, 4, 5)
mixed_tuple = (1, "hello", 3.5, True)
```

### **2.2 Accessing Tuple Elements**
Indexing and slicing work the same as in lists.
```python
# Indexing
print(my_tuple[0])   # Output: 1
print(my_tuple[-1])  # Output: 5

# Slicing
print(my_tuple[1:4]) # Output: (2, 3, 4)
```

### **2.3 Tuple Methods**
| Method | Description | Example |
|--------|------------|---------|
| `count(x)` | Returns the number of times `x` appears | `tuple.count(2)` |
| `index(x)` | Returns the index of first occurrence of `x` | `tuple.index(3)` |

### **2.4 Modifying a Tuple**
Tuples **cannot** be modified.
```python
my_tuple[2] = 10  # TypeError: 'tuple' object does not support item assignment
```
However, tuples can store **mutable** objects like lists.
```python
nested_tuple = (1, [2, 3], 4)
nested_tuple[1].append(5)  # Modifies the list inside tuple
print(nested_tuple)  # Output: (1, [2, 3, 5], 4)
```
# **Operations with Tuples in Python**  

Tuples support various operations like indexing, slicing, concatenation, repetition, membership testing, and iteration. Below is a detailed explanation of tuple operations with examples.

---

## **1. Concatenation (`+`)**
You can combine two tuples using the `+` operator. This creates a new tuple.

```python
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
result = tuple1 + tuple2
print(result)  # Output: (1, 2, 3, 4, 5, 6)
```

---

## **2. Repetition (`*`)**
You can repeat a tuple multiple times using the `*` operator.

```python
my_tuple = (1, 2, 3)
repeated_tuple = my_tuple * 3
print(repeated_tuple)  # Output: (1, 2, 3, 1, 2, 3, 1, 2, 3)
```

---

## **3. Indexing (`[]`)**
Tuples support **indexing** to access elements. Indexing starts at `0`.

```python
my_tuple = ('a', 'b', 'c', 'd')
print(my_tuple[0])   # Output: 'a'
print(my_tuple[-1])  # Output: 'd' (negative index)
```

---

## **4. Slicing (`[:]`)**
Tuples support **slicing** to extract a sub-part of the tuple.

```python
my_tuple = (10, 20, 30, 40, 50)
print(my_tuple[1:4])   # Output: (20, 30, 40)
print(my_tuple[:3])    # Output: (10, 20, 30)
print(my_tuple[2:])    # Output: (30, 40, 50)
print(my_tuple[::-1])  # Output: (50, 40, 30, 20, 10) (reverse tuple)
```

---

## **5. Length (`len()`)**
You can find the number of elements in a tuple using `len()`.

```python
my_tuple = (1, 2, 3, 4, 5)
print(len(my_tuple))  # Output: 5
```

---

## **6. Membership Testing (`in`, `not in`)**
You can check if an element exists in a tuple.

```python
my_tuple = ('apple', 'banana', 'cherry')

print('apple' in my_tuple)   # Output: True
print('orange' not in my_tuple)  # Output: True
```

---

## **7. Iteration (Looping Through a Tuple)**
You can iterate through a tuple using a `for` loop.

```python
my_tuple = (10, 20, 30, 40)

for item in my_tuple:
    print(item)
```
**Output:**
```
10
20
30
40
```

---

## **8. Tuple Packing and Unpacking**
### **Packing:**
You can store multiple values inside a tuple.

```python
packed_tuple = 1, 2, 3, 4
print(packed_tuple)  # Output: (1, 2, 3, 4)
```

### **Unpacking:**
You can extract values from a tuple into separate variables.

```python
my_tuple = (10, 20, 30)
a, b, c = my_tuple
print(a, b, c)  # Output: 10 20 30
```

---

## **9. Finding Minimum and Maximum (`min()`, `max()`)**
You can get the smallest and largest values in a tuple.

```python
numbers = (3, 7, 1, 9, 4)
print(min(numbers))  # Output: 1
print(max(numbers))  # Output: 9
```

---

## **10. Counting Occurrences (`count()`)**
Find how many times an element appears in a tuple.

```python
my_tuple = (1, 2, 3, 1, 1, 4)
print(my_tuple.count(1))  # Output: 3
```

---

## **11. Finding Index (`index()`)**
Find the position of an element in a tuple.

```python
my_tuple = (10, 20, 30, 40)
print(my_tuple.index(30))  # Output: 2
```

---

## **12. Converting List to Tuple and Vice Versa**
You can convert a list to a tuple and vice versa using `tuple()` and `list()`.

```python
# Convert list to tuple
my_list = [1, 2, 3, 4]
tuple_from_list = tuple(my_list)
print(tuple_from_list)  # Output: (1, 2, 3, 4)

# Convert tuple to list
my_tuple = (5, 6, 7, 8)
list_from_tuple = list(my_tuple)
print(list_from_tuple)  # Output: [5, 6, 7, 8]
```

---

### **Conclusion**
- **Tuples support various operations like indexing, slicing, concatenation, and repetition.**
- **Tuples are immutable, meaning elements cannot be modified after creation.**
- **They are useful when you want to store fixed data efficiently.**

---

## **3. Differences Between Lists and Tuples**

| Feature | List | Tuple |
|---------|------|-------|
| **Mutability** | Mutable (can be changed) | Immutable (cannot be changed) |
| **Syntax** | `[]` (square brackets) | `()` (parentheses) |
| **Performance** | Slower (due to mutability) | Faster (fixed size) |
| **Methods** | Many built-in methods | Limited methods (`count()`, `index()`) |
| **Use Case** | When data changes frequently | When data should remain constant |

---

## **4. Difference Between Strings and Lists**
| Feature | String | List |
|---------|--------|------|
| **Mutability** | Immutable | Mutable |
| **Indexing** | Supports indexing | Supports indexing |
| **Modification** | Cannot modify elements directly | Can modify elements directly |
| **Methods** | Many built-in string methods (`upper()`, `lower()`, `split()`, etc.) | List manipulation methods (`append()`, `remove()`, `sort()`, etc.) |
| **Concatenation** | Uses `+` to join strings | Uses `+` to merge lists |
| **Iteration** | Iterates character by character | Iterates element by element |

### **Example**
```python
# Strings are immutable
s = "hello"
# s[0] = "H"  # Error: Strings cannot be modified

# Lists are mutable
l = ["h", "e", "l", "l", "o"]
l[0] = "H"
print(l)  # Output: ['H', 'e', 'l', 'l', 'o']
```

---

### **Conclusion**
- **Lists** are mutable, versatile, and commonly used for dynamic data.
- **Tuples** are immutable, faster, and used when data should not change.
- **Strings** are immutable like tuples, whereas **lists** are mutable.

