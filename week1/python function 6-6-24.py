# 1.Functions in Python
'''user defined function in python are function which are made by user with their specific user codes basically these function are made to decrease time and to decrease 
complexity of a program by allowing user to  developers to break down complex tasks into smaller, more manageable pieces, making the code easier to understand, maintain, and debug.
'''
#properites of function:-
'''1:- def keyword:- this def is used for defining the function
2:- Function: use lowercase with underscores fpr seperation.
3:-Parantheses ():These enclose any parameters(arguments) the function might accept  if the function doesnt take any arguments you will still have empty arguments.
4:-Colon: This follows the paranthesis and indicates the start of the function body.
5:-Indented Block: The indented block (usually 4 spaces or a tab)contains the statements that define the functions behaviour.This block can include calculations, variable assignments, conditional statements.
6:-Optional return Statement: This statement (if present) specifies the value the function will return when called If no return statement is present the function implicityly returns None'''

# Note:- to access function specialities we have to call the fuction name
#example:-

def add_numbers(a, b):
    return a + b
result = add_numbers(3, 5)
print("The sum of 3 and 5 is:", result)

# parameter in functions
'''Parameters is  also known as argumentsthey  are the inputs a function receives when it's called. They provide a way to customize the function's behavior for different scenarios. Here's a breakdown of different types of parameters in Python:
'''
'''1.)positional arguments:-
These are arguments passed to the function in the same order they are defined in the function declaration. The function expects a specific number of arguments based on the order.
example:-'''
def calculate_area(length, width):
    area = length * width
    return area
length = 5
width = 3
area = calculate_area(length, width)
print("The area of a rectangle with length {} and width {} is: {}".format(length, width, area))

#2.) keyword arguments:-
'''These arguments are passed by name when calling the function. The order doesn't matter as long as you associate the value with the correct parameter name.'''
# example:-
def calculate_area(length, width):
    area = length * width
    return area
area1 = calculate_area(length=5, width=3)
area2 = calculate_area(width=4, length=6)
print("The area of a rectangle with length 5 and width 3 is:", area1)
print("The area of a rectangle with length 6 and width 4 is:", area2)

'''3) Variable Length Arguments (args):- This allows a function to accept an arbitrary number of positional arguments. These arguments are packed into a tuple inside the function.
'''
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

'''4.) Keyword Variable Length Arguments (kwargs) Similar to variable length arguments, but these arguments are captured in a dictionary. You can pass any number of keyword arguments, and they are accessible as key-value pairs within the function.
'''
example:-
def print_person_info(name, age, **kwargs):
    print("Name:", name)
    print("Age:", age)
    if kwargs:
        print("Additional Information:")
        for key, value in kwargs.items():
            print(f"{key}: {value}")
print_person_info("Alice", 30, city="New York", occupation="Engineer")

#lambda function
'''in Python a lambda function is a small anonymous function defined using the lambda keyword. Lambda functions can take any number of arguments, but they can only have one expression. They are often used as a shortcut for simple functions where defining a full function using def is unnecessary or cumbersome.
'''
# syntax:-lambda arguments : expression
#example :-
add = lambda x, y: x + y
print(add(2, 3))  # Output: 5


# question :- sorting using lambda function:-
numbers = input("Enter a list of numbers separated by spaces: ").split()
numbers = [int(num) for num in numbers]
sorted_numbers = sorted(numbers, key=lambda x: x)
print("Sorted numbers:", sorted_numbers)

'''Key Points about Lambda Function:-
1.They are ideal for short and simple expressions
2.They cannot contain complex statements like if or for loops
3.They are often used for quick  throwaway functions withing larger expressions
4.They can be a powerful tool when used appropriately but they might not always be the most readable option for complex logic
'''


# map function:-The map() function returns an iterator that yields the results of applying the specified function to each element of the iterable one by one.
'''It takes two arguments:
A function to be applied to each element. This can be a named function or a lambda function
An iterable (list, tuple, etc.) containing the elements to be processed'''
#example:-
def square(x):
    return x ** 2
numbers = [1, 2, 3, 4, 5]
squared_numbers = map(square, numbers)
print(list(squared_numbers))  # Output: [1, 4, 9, 16, 25]



# filter function:- the filter() function is a builtin function used to filter elements from an iterable (such as a list tupleor string) based on a specified condition
def is_even(num):
    return num % 2 == 0
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = filter(is_even, numbers)
print(list(even_numbers))  # Output: [2, 4, 6, 8, 10]


# reduce function:-The reduce() function applies a function of two arguments cumulatively to the items of an iterable, from left to right, so as to reduce the iterable to a single value.
# syntax:- functools.reduce(function, iterable[, initializer])
from functools import reduce

# Define a function to add two numbers
def add(x, y):
    return x + y
numbers = [1, 2, 3, 4, 5]
sum_of_numbers = reduce(add, numbers)
print("Sum of numbers:", sum_of_numbers)  # Output: 15
