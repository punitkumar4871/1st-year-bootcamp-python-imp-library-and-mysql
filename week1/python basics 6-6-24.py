# Input and Output in Python
# output function
''' output function in python:- This function allows us to display text, variables.'''
# note :- if u want to print same expression like u want put it in "" and if u want to print variable value then no need to do that
'''example'''
print("Hello, World!")
'''example2'''
name = "Alice"
age = 30
print("Name:", name, "Age:", age)

# input function:-
### input function allow user to give input 
''' disadvantage:- take every function in form of string i.e 3+3 =33'''
#### int function it is used to give value in form interger

# Taking input from the user
num = int(input("Enter a value: "))

add = num + 5

# Output
print("The sum is %d" %add)

# data type
# Numeric types (int, float, complex) are immutable, meaning their values cannot be changed after creation.
# Sequence types (str, list, tuple) can contain multiple values of different data types.
# range is a special sequence type that generates a sequence of numbers within a specified range.
# Mapping types (dict) store key-value pairs, where keys must be unique and immutable.
# Set types (set, frozenset) are unordered collections of unique elements.
# The bool type represents truth values (True or False).'''
int_num = 42      # these are interger
float_num = 3.14159    # float contain decimals
complex_num = 1 + 2j    # it contain complex number as root -1

string = "Python is awesome!"    # it sontain string value
boolean = True  # boolean contain true and false
list_example = [10, "text", 3.14, [1, 2, 3]]    # it contain valuein [] these brakcets
tuple_example = (20, "tuple", 7.5)   # this contain value in ()
range_example = range(1, 10)       # this contain value form intial range to final range
dict_example = {"name": "Alice", "age": 25, "city": "Wonderland"}    # it conatin value stored form key and value
set_example = {1, 2, 3, 4, 5}   # contain in {}
frozenset_example = frozenset([1, 2, 3, 4, 5])    # contian in mix brakcet format

# operators:- in python are used to do certain operations in pythons

# An expression:- in Python is a combination of values, variables, operators, and function calls that are evaluated to produce a new value. Expressions are fundamental building blocks in Python programming, allowing you to perform calculations, manipulate data, and determine control flow.

# Expressions and Operators
a = 10
b = 3

# Arithmetic Operators
print(a + b)  # Addition: 13
print(a - b) # Subtraction: 7
print(a * b)    # Multiplcation: 30
print(a / b) # Divisin: 3.3333333333333335
print(a // b) # Floor Division: 3
print(a % b)  # Modlus: 1
print(a ** b)  # Expo'entiation: 1000

# Comparison Operators
print(a == b) # Equal to: False
print(a != b) # Not equal to: True
print(a > b)  # Greater than: True
print(a < b)  # Less than: False
print(a >= b) # Greater than or equal to: True
print(a <= b) # Less than or equal to: False

# Logical Operators
print(a > 5 and b < 5)  # and: True
print(a > 5 or b < 1)   # or: True
print(not(a > 5 and b < 5)) # not: False

# code:-
a = 7
b = 2

# addition
print ('Sum: ', a + b)  

# subtraction
print ('Subtraction: ', a - b)   

# multiplication
print ('Multiplication: ', a * b)  

# division
print ('Division: ', a / b) 

# floor division
print ('Floor Division: ', a // b)

# modulo
print ('Modulo: ', a % b)  

# a to the power b
print ('Power: ', a ** b) 

# conditional statements
'''Conditional Statements
The if statement executes a block of code if a specified condition is true.
The elif (short for "else if") statement provides additional conditions to check if the previous conditions were false.
The else statement specifies a block of code to execute if none of the previous conditions were true.
Conditions in if, elif, and else statements must evaluate to a boolean value (True or False).'''
# example
number = 15
if number > 20:
    print("The number is greater than 20.")
elif number > 10:
    print("The number is greater than 10 but less than or equal to 20.")
elif number > 5:
    print("The number is greater than 5 but less than or equal to 10.")
else:
    print("The number is 5 or less.")

# looping statement :- these are used to implement thing until the condtion is true or limit is reached
# these are of 2 types :- 1.) while looping 2.) for looping
# example of while looping:- this a looping statement which work on condition

while number <= 5:
    print(number)
    number += 1  # Increment the number by 1

# example of for looping statement:-
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number)


# jumping statements:-
''' jumping statement are of 2 type:_
1.) break:- it terminate the loop
2.) continue:- it skip when some condition get true'''
# example:-
print("Using break:")
# Use a for loop to print numbers until a certain condition is met
for number in numbers:
    if number == 6:
        break  # Exit the loop when the number is 6
    print(number)

print("\nUsing continue:")
# Use a for loop to skip printing certain numbers
for number in numbers:
    if number % 2 == 0:
        continue  # Skip the rest of the loop body for even numbers
    print(number)


# special function
''' some special function of python are:-
1.) len:-can be used to calculate length of our data structure 
2.)id:-function returns the unique identifier (memory address) of an object.
3.)type:-tell the type of a variable used 
4.)range:- used to print value from a specific range



