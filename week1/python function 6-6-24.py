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
