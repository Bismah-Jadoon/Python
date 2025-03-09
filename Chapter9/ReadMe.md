# File Input/Output (I/O) in Python

File I/O in Python allows users to read from and write to files. This is essential for handling persistent data, configuration files, logs, and more.

## Opening a File
In Python, files are opened using the built-in `open()` function. The syntax is:
```python
file = open("filename", "mode")
```

### File Opening Modes
| Mode | Description |
|------|-------------|
| `r`  | Read mode (default). The file must exist. |
| `w`  | Write mode. Creates a new file or truncates an existing file. |
| `a`  | Append mode. Data is added to the end of the file. |
| `x`  | Exclusive creation. Fails if the file exists. |
| `b`  | Binary mode. Used with other modes (e.g., `rb` or `wb`). |
| `t`  | Text mode (default). Used with other modes (e.g., `rt` or `wt`). |
| `+`  | Read and write mode. Used with `r+`, `w+`, or `a+`. |

## Reading from a File
### Reading the Entire File
```python
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
```

### Reading Line by Line
```python
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())
```

### Reading Specific Number of Characters
```python
with open("example.txt", "r") as file:
    content = file.read(10)  # Reads first 10 characters
    print(content)
```

### Using `readlines()`
```python
with open("example.txt", "r") as file:
    lines = file.readlines()
    print(lines)  # List of all lines
```

## Writing to a File
### Writing with `w` Mode (Overwrites File)
```python
with open("output.txt", "w") as file:
    file.write("Hello, World!\n")
```

### Writing with `a` Mode (Appending)
```python
with open("output.txt", "a") as file:
    file.write("Appending a new line.\n")
```

### Writing Multiple Lines with `writelines()`
```python
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open("output.txt", "w") as file:
    file.writelines(lines)
```

## Working with Binary Files
### Reading a Binary File
```python
with open("image.jpg", "rb") as file:
    binary_data = file.read()
```

### Writing a Binary File
```python
with open("copy.jpg", "wb") as file:
    file.write(binary_data)
```

## File Handling Best Practices
### Using `with` Statement
Using the `with` statement ensures that files are properly closed after execution.
```python
with open("file.txt", "r") as file:
    content = file.read()
```

### Closing a File Manually
If not using `with`, always close the file.
```python
file = open("file.txt", "r")
content = file.read()
file.close()
```

## Checking if a File Exists
Using the `os` module:
```python
import os
if os.path.exists("file.txt"):
    print("File exists")
else:
    print("File does not exist")
```

Using `pathlib`:
```python
from pathlib import Path
if Path("file.txt").exists():
    print("File exists")
```

## Deleting a File
```python
import os
if os.path.exists("file.txt"):
    os.remove("file.txt")
```

## Exception Handling in File I/O
```python
try:
    with open("non_existent.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found!")
except IOError:
    print("I/O error occurred!")
```

## Conclusion
File I/O in Python is a fundamental concept used in data processing and storage. The `open()` function provides various modes for reading, writing, and manipulating files efficiently. Always handle files properly using `with` statements and error handling to prevent issues.


