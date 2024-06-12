# Python Dictionaries

## Introduction

A dictionary in Python is an unordered collection of key-value pairs. It is a mutable data type, which means you can add, modify, or remove elements after its creation. Dictionaries are useful for storing and retrieving data in an efficient and flexible way, particularly when you need to associate values with unique keys.

## Creating a Dictionary

You can create a dictionary using the `dict()` constructor or by enclosing key-value pairs inside curly braces `{}`.

```python
# Using the dict() constructor
empty_dict = dict()
```

# Using curly braces
student = {'name': 'Alice', 'age': 22, 'university': 'MIT'}
 # Accessing and Modifying Values
You can access values in a dictionary using their corresponding keys.


```python
Copy code
# Accessing values
print(student['name'])  # Output: Alice
print(student.get('age'))  # Output: 22
```

# Modifying values
```python 
student['age'] = 23
print(student)  # Output: {'name': 'Alice', 'age': 23, 'university': 'MIT'}
```
# Dictionary Methods
### Dictionaries provide several built-in methods for working with them efficiently:

1.)keys(): Returns a view object containing the dictionary's keys.
2.)values(): Returns a view object containing the dictionary's values.
3.)items(): Returns a view object that displays a list of all the values in the dictionary.
4.)get(key, default=None): Returns the value for the specified key if the key is in the dictionary. If the key is not found, it returns the default value provided as the second argument (None if not specified).
5.)pop(key, default=None): Removes the key-value pair from the dictionary and returns the value. If the key is not found, it returns the default value provided as the second argument (raises a KeyError if not specified).
6.)clear(): Removes all the key-value pairs from the dictionary.
7.)copy(): Returns a shallow copy of the dictionary.
### Examples
```python
# Dictionary for demonstration
person = {'name': 'Bob', 'age': 35, 'city': 'Chicago'}

# keys()
print(person.keys())  # Output: dict_keys(['name', 'age', 'city'])

# values()
print(person.values())  # Output: dict_values(['Bob', 35, 'Chicago'])

# items()
print(person.items())  # Output: dict_items([('name', 'Bob'), ('age', 35), ('city', 'Chicago')])

# get()
print(person.get('name'))  # Output: Bob
print(person.get('phonenumber', 'Not Available'))  # Output: Not Available

# pop()
removed_value = person.pop('age')
print(removed_value)  # Output: 35
print(person)  # Output: {'name': 'Bob', 'city': 'Chicago'}

# clear()
person.clear()
print(person)  # Output: {}

# copy()
new_dict = student.copy()
print(new_dict)  # Output: {'name': 'Alice', 'age': 23, 'university': 'MIT'}
```
### Adding and Removing Key-Value Pairs
```python
# Adding a new pair
student['email'] = 'alice@example.com'
print(student)  # Output: {'name': 'Alice', 'age': 23, 'university': 'MIT', 'email': 'alice@example.com'}

# Removing a pair
popped_value = student.pop('university')
print(popped_value)  # Output: MIT
print(student)  # Output: {'name': 'Alice', 'age': 23, 'email': 'alice@example.com'}
```
## Dictionary Comprehension
Dictionary comprehension is a concise way to create a new dictionary from an iterable.

### Examples
Creating a dictionary from a list

```python
# List of numbers
numbers = [1, 2, 3, 4, 5]

# Dictionary with squares of numbers
squares = {num: num**2 for num in numbers}
print(squares)  # Output: {1: 1, 2: 4, 3
```


## Creating a dictionary from another dictionary

```python

# Original dictionary
original = {'a': 1, 'b': 2, 'c': 3}

# New dictionary with keys and values swapped
swapped = {value: key for key, value in original.items()}
print(swapped)  # Output: {1: 'a', 2: 'b', 3: 'c'}
```
## Creating a dictionary with conditional logic

```python
# List of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Dictionary with even numbers as keys and their cubes as values
even_cubes = {num: num**3 for num in numbers if num % 2 == 0}
print(even_cubes)  # Output: {2: 8, 4: 64, 6: 216, 8: 512, 10: 1000}
```
## Creating a dictionary from two lists

```python
# List of keys
keys = ['a', 'b', 'c', 'd', 'e']

# List of values
values = [1, 2, 3, 4, 5]

# Dictionary from keys and values
new_dict = {key: value for key, value in zip(keys, values)}
print(new_dict)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
```
## Nesting Dictionaries
Dictionaries can contain other dictionaries as values, creating nested structures.

```python

student = {
    'name': 'Alice',
    'age': 23,
    'contact': {
        'email': 'alice@example.com',
        'phone': '555-1234'
    }
}

print(student['contact']['email'])  # Output: alice@example.com
```
## Practical Examples and Use Cases
### Counting Occurrences
Dictionaries can be used to count the occurrences of elements in a collection.

```python
# Counting word occurrences in a sentence
sentence = "Python is great. Python is dynamic. Python is simple."
word_counts = {}

for word in sentence.split():
    word = word.strip(".")
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

print(word_counts)  # Output: {'Python': 3, 'is': 3, 'great': 1, 'dynamic': 1, 'simple': 1}
```
## Data Manipulation and Filtering
Dictionaries are useful for data manipulation, filtering, and analysis tasks.

# Data Manipulation
Transforming a list of dictionaries into a dictionary of lists, grouped by a specific key.

```python

# List of dictionaries
students = [
    {"name": "Alice", "age": 23, "university": "MIT"},
    {"name": "Bob", "age": 24, "university": "Stanford"},
    {"name": "Charlie", "age": 22, "university": "MIT"},
    {"name": "David", "age": 25, "university": "Stanford"}
]
# Grouping data by university
grouped_data = {}
for student in students:
    university = student["university"]
    if university in grouped_data:
        grouped_data[university].append(student)
    else:
        grouped_data[university] = [student]

print(grouped_data)
# Output:
# {'MIT': [{'name': 'Alice', 'age': 23, 'university': 'MIT'}, {'name': 'Charlie', 'age': 22, 'university': 'MIT'}],
#  'Stanford': [{'name': 'Bob', 'age': 24, 'university': 'Stanford'}, {'name': 'David', 'age': 25, 'university': 'Stanford'}]}
```
# Data Filtering
Filtering a list of dictionaries to include only those with an age greater than 23.

```python

# List of dictionaries
students = [
    {"name": "Alice", "age": 23, "university": "MIT"},
    {"name": "Bob", "age": 24, "university": "Stanford"},
    {"name": "Charlie", "age": 22, "university": "MIT"},
    {"name": "David", "age": 25, "university": "Stanford"}
]

# Filtering data based on age
filtered_students = [student for student in students if student["age"] > 23]

print(filtered_students)  # Output: [{'name': 'Bob', 'age': 24, 'university': 'Stanford'}, {'name': 'David', 'age': 25, 'university': 'Stanford'}]
```
# Data Analysis
Calculating the average age of students in each university.

```python

# List of dictionaries
students = [
    {"name": "Alice", "age": 23, "university": "MIT"},
    {"name": "Bob", "age": 24, "university": "Stanford"},
    {"name": "Charlie", "age": 22, "university": "MIT"},
    {"name": "David", "age": 25, "university": "Stanford"}
]

# Grouping data by university and calculating average age
university_ages = {}
for student in students:
    university = student["university"]
    if university in university_ages:
        university_ages[university].append(student["age"])
    else:
        university_ages[university] = [student["age"]]

average_ages = {university: sum(ages)/len(ages) for university, ages in university_ages.items()}

print(average_ages)  # Output: {'MIT': 22.5, 'Stanford': 24.5}
```