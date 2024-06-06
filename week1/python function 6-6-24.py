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
