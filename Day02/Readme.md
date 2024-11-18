# Day 2 - Python Training: Dictionaries, Sets, Operators, If-Else, Functions & Pandas

### Overview:
This document outlines the key topics covered on **Day 2** of the training, including:

- Python operators
- Conditional statements (`if-else` blocks)
- Functions
- Introduction to **Pandas** for data manipulation and analysis
- Working with **Dictionaries** and **Sets**

### Topics Covered:

---

## 1. **Operators in Python**

Operators are symbols that perform operations on variables and values. Python supports various types of operators:

### 1.1 Arithmetic Operators
Used to perform basic arithmetic operations.
- `+` : Addition
- `-` : Subtraction
- `*` : Multiplication
- `/` : Division
- `//` : Floor Division
- `%` : Modulo (remainder of division)
- `**` : Exponentiation (power)

### 1.2 Assignment Operators
Used to assign values to variables, and to perform operations while assigning.
- `=` : Assign a value
- `+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `**=`: Assign and operate on the variable's value.

### 1.3 Comparison Operators
Used to compare two values and return a boolean (`True` or `False`).
- `==` : Equal to
- `!=` : Not equal to
- `>` : Greater than
- `<` : Less than
- `>=` : Greater than or equal to
- `<=` : Less than or equal to

### 1.4 Logical Operators
Used to combine conditional statements.
- `and` : Returns `True` if both conditions are `True`
- `or` : Returns `True` if at least one condition is `True`
- `not` : Reverses the boolean value (e.g., `not True` is `False`)

### 1.5 Identity Operators
Used to compare the memory locations of two objects.
- `is` : Returns `True` if both variables point to the same object in memory
- `is not` : Returns `True` if both variables do not point to the same object

### 1.6 Membership Operators
Used to test if a value is found in a sequence (such as a list, tuple, or string).
- `in` : Returns `True` if the value exists in the sequence
- `not in` : Returns `True` if the value does not exist in the sequence

### 1.7 Bitwise Operators
Used to perform bit-level operations on integers.
- `&` : AND
- `|` : OR
- `^` : XOR (exclusive OR)
- `~` : NOT
- `<<` : Left shift
- `>>` : Right shift

---

## 2. **If-Else Statements**

Conditional statements are used to perform different actions based on different conditions.

- `if`: Used to test a condition.
- `elif`: Used to test another condition if the `if` condition is `False`.
- `else`: Used to execute a block of code if none of the `if` or `elif` conditions are `True`.

---

## 3. **Functions in Python**

A function is a reusable block of code that performs a specific task. Functions allow you to group related code and execute it when needed.

- **Defining a Function**: Functions are defined using the `def` keyword.
- **Return Values**: Functions can return values using the `return` keyword.
- **Parameters**: Functions can accept input values, known as parameters, to work with within the function.

---

## 4. **Introduction to Pandas**

[Pandas](https://pandas.pydata.org/) is a Python library used for data manipulation and analysis. It provides two main data structures:

### 4.1 DataFrame
A DataFrame is a 2-dimensional labeled data structure, similar to a table in a database or an Excel spreadsheet. It allows you to store and manipulate large datasets with rows and columns.

### 4.2 Series
A Series is a one-dimensional labeled array capable of holding any data type. It can be thought of as a single column of data.

### 4.3 Common Pandas Operations
- **Reading Data**: The `read_csv()` function is used to read data from a CSV file into a DataFrame.
- **Viewing Data**: The `.head()` method returns the first 5 rows of a DataFrame, while `.tail()` returns the last 5 rows.
- **Descriptive Statistics**: The `.describe()` method provides summary statistics of the DataFrame, including count, mean, std (standard deviation), min, and max values.
- **Data Information**: The `.info()` method provides a concise summary of a DataFrame, including the number of non-null entries and data types.
- **Shape**: The `.shape` attribute returns the number of rows and columns in a DataFrame.

---

## 5. **Dictionaries and Sets in Python**

### 5.1 Dictionaries
A dictionary is an unordered collection of key-value pairs. Each key is unique, and values can be of any data type.

- **Definition**: Defined using curly braces `{}` with key-value pairs separated by a colon `:`.
- **Use**: To store data in a way that allows for fast lookups based on a key.

### 5.2 Sets
A set is an unordered collection of unique elements. Sets do not allow duplicates and are commonly used for membership testing.

- **Definition**: Defined using curly braces `{}` or the `set()` constructor.
- **Use**: To perform set operations such as union, intersection, and difference.

---

### Summary:

- **Operators**: Python supports a variety of operators, including arithmetic, assignment, comparison, logical, and more.
- **Conditional Statements**: `if-else` blocks allow branching based on conditions.
- **Functions**: Functions are reusable blocks of code that accept inputs and return outputs.
- **Pandas**: The Pandas library is essential for data manipulation, with its key structures being DataFrames and Series.
- **Dictionaries & Sets**: Dictionaries store key-value pairs, while sets store unique, unordered elements.

---

This concludes the Day 2 session on Python. Make sure to practice these concepts by writing code and experimenting with examples. If you have any questions, feel free to ask! 

