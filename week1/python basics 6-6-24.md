# Input and Output in Python

## Output Function
Output function in Python allows us to display text, variables.

### Note:
If you want to print the same expression like you want, put it in quotes `""`. If you want to print a variable value, then there's no need to do that.

### Example
```python
print("Hello, World!")
```

### Example 2
```python
name = "Alice"
age = 30
print("Name:", name, "Age:", age)
```

## Input Function
The input function allows the user to give input.

### Disadvantage:
Takes every input in the form of a string, i.e., `3+3` = `"33"`

### int Function
Used to convert input into an integer.

### Example
```python
num = int(input("Enter a value: "))
add = num + 5

# Output
print("The sum is %d" % add)
```

## Data Types

### Numeric Types
- `int` : Immutable integer.
- `float` : Contains decimal values.
- `complex` : Contains complex numbers.

### Sequence Types
- `str` : String value.
- `list` : List of multiple values.
- `tuple` : Tuple of multiple values.
- `range` : Generates a sequence of numbers.

### Mapping Types
- `dict` : Key-value pairs.

### Set Types
- `set` : Unordered collection of unique elements.
- `frozenset` : Immutable version of a set.

### Boolean Type
- `bool` : Represents `True` or `False`.

### Examples
```python
int_num = 42
float_num = 3.14159
complex_num = 1 + 2j

string = "Python is awesome!"
boolean = True
list_example = [10, "text", 3.14, [1, 2, 3]]
tuple_example = (20, "tuple", 7.5)
range_example = range(1, 10)
dict_example = {"name": "Alice", "age": 25, "city": "Wonderland"}
set_example = {1, 2, 3, 4, 5}
frozenset_example = frozenset([1, 2, 3, 4, 5])
```

## Operators
Operators in Python are used to perform operations.

### Arithmetic Operators
```python
a = 10
b = 3

print(a + b)  # Addition: 13
print(a - b)  # Subtraction: 7
print(a * b)  # Multiplication: 30
print(a / b)  # Division: 3.3333333333333335
print(a // b) # Floor Division: 3
print(a % b)  # Modulus: 1
print(a ** b) # Exponentiation: 1000
```

### Comparison Operators
```python
print(a == b)  # Equal to: False
print(a != b)  # Not equal to: True
print(a > b)   # Greater than: True
print(a < b)   # Less than: False
print(a >= b)  # Greater than or equal to: True
print(a <= b)  # Less than or equal to: False
```

### Logical Operators
```python
print(a > 5 and b < 5)    # and: True
print(a > 5 or b < 1)     # or: True
print(not(a > 5 and b < 5)) # not: False
```

### Example Code
```python
a = 7
b = 2

print('Sum: ', a + b)
print('Subtraction: ', a - b)
print('Multiplication: ', a * b)
print('Division: ', a / b)
print('Floor Division: ', a // b)
print('Modulo: ', a % b)
print('Power: ', a ** b)
```

## Conditional Statements
Conditional statements execute code based on specific conditions.

### Example
```python
number = 15
if number > 20:
    print("The number is greater than 20.")
elif number > 10:
    print("The number is greater than 10 but less than or equal to 20.")
elif number > 5:
    print("The number is greater than 5 but less than or equal to 10.")
else:
    print("The number is 5 or less.")
```

## Looping Statements
Looping statements are used to execute a block of code repeatedly.

### While Loop
Executes a block of code as long as a condition is true.

### Example
```python
number = 1
while number <= 5:
    print(number)
    number += 1  # Increment the number by 1
```

### For Loop
Executes a block of code for each item in a sequence.

### Example
```python
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number)
```

## Jumping Statements
Jumping statements are used to alter the flow of control in loops.

### Types:
1. **break** : Terminates the loop.
2. **continue** : Skips the rest of the loop body for the current iteration.

### Example
```python
print("Using break:")
for number in numbers:
    if number == 3:
        break  # Exit the loop when the number is 3
    print(number)

print("\nUsing continue:")
for number in numbers:
    if number % 2 == 0:
        continue  # Skip the rest of the loop body for even numbers
    print(number)
```

## Special Functions
### Some special functions in Python are:
1. **len** : Calculates the length of a data structure.
2. **id** : Returns the unique identifier (memory address) of an object.
3. **type** : Tells the type of a variable.
4. **range** : Generates a sequence of numbers.
