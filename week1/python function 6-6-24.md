# 1. Functions in Python

User-defined functions in Python are functions created by the user to encapsulate specific code. These functions reduce complexity and enhance code readability by breaking down complex tasks into manageable pieces.

## Properties of Functions:
1. **def keyword**: Used to define the function.
2. **Function Naming**: Use lowercase with underscores for separation.
3. **Parentheses ()**: Enclose any parameters (arguments) the function might accept. If the function doesn’t take any arguments, you will still have empty parentheses.
4. **Colon**: Indicates the start of the function body.
5. **Indented Block**: Contains the statements that define the function's behavior. This block can include calculations, variable assignments, and conditional statements.
6. **Optional return Statement**: Specifies the value the function will return when called. If no return statement is present, the function implicitly returns `None`.

### Note:
To access a function's functionalities, we need to call the function by its name.

### Example:
```python
def add_numbers(a, b):
    return a + b

result = add_numbers(3, 5)
print("The sum of 3 and 5 is:", result)
```

## Parameters in Functions

Parameters, also known as arguments, are inputs a function receives when it's called. They customize the function's behavior for different scenarios.

### 1. Positional Arguments:
These are arguments passed to the function in the same order they are defined in the function declaration.

#### Example:
```python
def calculate_area(length, width):
    area = length * width
    return area

length = 5
width = 3
area = calculate_area(length, width)
print("The area of a rectangle with length {} and width {} is: {}".format(length, width, area))
```

### 2. Keyword Arguments:
These arguments are passed by name when calling the function. The order doesn’t matter as long as you associate the value with the correct parameter name.

#### Example:
```python
def calculate_area(length, width):
    area = length * width
    return area

area1 = calculate_area(length=5, width=3)
area2 = calculate_area(width=4, length=6)
print("The area of a rectangle with length 5 and width 3 is:", area1)
print("The area of a rectangle with length 6 and width 4 is:", area2)
```

### 3. Variable Length Arguments (`*args`):
Allows a function to accept an arbitrary number of positional arguments. These arguments are packed into a tuple inside the function.

#### Example:
```python
def sum_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

result1 = sum_numbers(1, 2, 3)
result2 = sum_numbers(4, 5, 6, 7)
result3 = sum_numbers(8, 9)
print("Sum of numbers:", result1)
print("Sum of numbers:", result2)
print("Sum of numbers:", result3)
```

### 4. Keyword Variable Length Arguments (`**kwargs`):
These arguments are captured in a dictionary. You can pass any number of keyword arguments, and they are accessible as key-value pairs within the function.

#### Example:
```python
def print_person_info(name, age, **kwargs):
    print("Name:", name)
    print("Age:", age)
    if kwargs:
        print("Additional Information:")
        for key, value in kwargs.items():
            print(f"{key}: {value}")

print_person_info("Alice", 30, city="New York", occupation="Engineer")
```

## Lambda Function
A lambda function is a small anonymous function defined using the `lambda` keyword. Lambda functions can take any number of arguments but can only have one expression.

### Syntax:
`lambda arguments : expression`

### Example:
```python
add = lambda x, y: x + y
print(add(2, 3))  # Output: 5
```

### Sorting Using Lambda Function:
```python
numbers = input("Enter a list of numbers separated by spaces: ").split()
numbers = [int(num) for num in numbers]
sorted_numbers = sorted(numbers, key=lambda x: x)
print("Sorted numbers:", sorted_numbers)
```

### Key Points about Lambda Function:
1. Ideal for short and simple expressions.
2. Cannot contain complex statements like `if` or `for` loops.
3. Often used for quick throwaway functions within larger expressions.
4. Powerful tool when used appropriately but may not always be the most readable option for complex logic.

## Map Function
The `map()` function returns an iterator that applies a specified function to each element of an iterable.

### Example:
```python
def square(x):
    return x ** 2

numbers = [1, 2, 3, 4, 5]
squared_numbers = map(square, numbers)
print(list(squared_numbers))  # Output: [1, 4, 9, 16, 25]
```

## Filter Function
The `filter()` function is a built-in function used to filter elements from an iterable based on a specified condition.

### Example:
```python
def is_even(num):
    return num % 2 == 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = filter(is_even, numbers)
print(list(even_numbers))  # Output: [2, 4, 6, 8, 10]
```

## Reduce Function
The `reduce()` function applies a function of two arguments cumulatively to the items of an iterable, reducing the iterable to a single value.

### Syntax:
`functools.reduce(function, iterable[, initializer])`

### Example:
```python
from functools import reduce

# Define a function to add two numbers
def add(x, y):
    return x + y

numbers = [1, 2, 3, 4, 5]
sum_of_numbers = reduce(add, numbers)
print("Sum of numbers:", sum_of_numbers)  # Output: 15
```

## Practice Questions

### 1. Calculate Area Function
Create a function `calculate_area(shape, dimensions)` that takes the shape (e.g., "rectangle", "circle") and its dimensions as arguments. The function should calculate the area based on the shape and return the result.

#### Example:
```python
import math

def calculate_area(shape, dimensions):
    if shape == "rectangle":
        length, width = dimensions
        return length * width
    elif shape == "circle":
        radius = dimensions
        return math.pi * radius ** 2
    else:
        return "Invalid shape"

print("Area of rectangle:", calculate_area("rectangle", (5, 3)))
print("Area of circle:", calculate_area("circle", 2))
```

### 2. Reverse Words Function
Create a function `reverse_words(text)` that takes a string as input and returns the string with the words reversed.

#### Example:
```python
def reverse_words(text):
    words = text.split()
    reversed_words = words[::-1]
    reversed_text = ' '.join(reversed_words)
    return reversed_text

text = "Hello world! This is a test."
print("Original text:", text)
print("Reversed text:", reverse_words(text))
```

### 3. Analyze List Function
Create a function `analyze_list(numbers)` that takes a list of numbers as input. The function should calculate and return the following in a dictionary:
- Minimum value in the list
- Maximum value in the list
- Average value of the list

#### Example:
```python
def analyze_list(numbers):
    if not numbers:
        return {"min": None, "max": None, "avg": None}

    min_value = min(numbers)
    max_value = max(numbers)
    avg_value = sum(numbers) / len(numbers)
    return {"min": min_value, "max": max_value, "avg": avg_value}

numbers = [1, 2, 3, 4, 5]
analysis = analyze_list(numbers)
print("Analysis:", analysis)
```

### 4. Filter Short Names Function
Create a list of product names (strings). Define a function `filter_short_names(names, max_length)` that takes the list of names and a maximum length as arguments. The function should return a list of names that are shorter than the specified maximum length.

#### Example:
```python
def filter_short_names(names, max_length):
    return list(filter(lambda name: len(name) < max_length, names))

product_names = ["Apple", "Banana", "Grapes", "Strawberry", "Pineapple"]
max_length = 6
short_names = filter_short_names(product_names, max_length)
print("Product names shorter than", max_length, "characters:", short_names)
```
