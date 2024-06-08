# Exception Handling in Python
Exception handling in Python allows a program to deal with unexpected situations (errors) gracefully. By handling exceptions you can ensure that your program can manage errors without crashing

# What is an Exception?
An exception is an event that disrupts the normal flow of a programs execution It is typically caused by errors such as division by zero, accessing a file that doesnt exist or running out of memory


# Basic Syntax:-
Python provides a way to handle exceptions using the try, except, else, and finally blocks. Here is a breakdown of how these blocks work:
1.)try: The code that might throw an exception is placed in this block.
2.)except: This block is executed if an exception occurs in the try block.
3.)else: This block is executed if no exceptions are raised in the try block.
4.)finally: This block is executed no matter what, whether an exception occurs or not.

# syntax
```python
try:
    # Code that might raise an exception
except SomeException as e:
    # Code that runs if the exception occurs
else:
    # Code that runs if no exception occurs
finally:
    # Code that always runs, regardless of an exception
```

# example 1:- learning syntax of exception handling 
```python
def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except TypeError:
        print("Error: Invalid input type. Please enter numbers.")
    else:
        print(f"The result is {result}.")
    finally:
        print("Execution complete.")

# Test cases
divide(10, 2)   
divide(10, 0)   
divide(10, 'a') 

```
# Explanation
### 1.)try block:-
 This is where you put the code that might raise an exception. In our example, it's result = a / b.
### 2.)except block:-
 This is where you handle the exception. You can have multiple except blocks for different types of exceptions. In our  example, we handle ZeroDivisionError and TypeError.
### 3.)else block:-
 If no exception occurs, the code inside the else block will be executed. In our example, it prints the result.
### 4.)finally block:- 
This block is always executed, regardless of whether an exception was raised or not. It's often used for cleanup actions like closing files or releasing resources. In our example, it prints "Execution complete."

# example 2:- implementing this on oops :-
```python
class CustomError(Exception):
    pass

def risky_function():
    try:
        # Some risky code
        raise CustomError("Something went wrong in risky_function")
    except CustomError as e:
        print(f"Caught an exception: {e}")

risky_function()
```

# Common Exception Classes
1.)ArithmeticError: Base class for errors occurring during numeric calculations.
2.)ZeroDivisionError: Raised when division by zero occurs.
3.)TypeError: Raised when an operation or function is applied to an object of inappropriate type.
4.)ValueError: Raised when a function receives an argument of the right type but inappropriate value.
5.)IndexError: Raised when attempting to access an index that is out of range.
6.)KeyError: Raised when attempting to access a dictionary key that does not exist.
7.)FileNotFoundError: Raised when a file or directory is requested but doesn’t exist.


# Best Practices
1. Be Specific with Exceptions
Catch specific exceptions rather than using a generic except block.
2. Use Finally for Cleanup
Use the finally block to clean up resources such as file handles or network connections.
3. Avoid Bare Except
Avoid using bare except clauses as they can catch unexpected exceptions and hide bugs.
4. Raise Meaningful Exceptions
Raise meaningful exceptions with informative error messages.
5. Log Exceptions
Log exceptions for better debugging and monitoring.




# questions :-
# Question 1
#### Write a function that takes two numbers as input and divides the first number by the second number. Raise a ZeroDivisionError if the second number is zero.
```python
def divide_numbers(num1, num2):
    if num2 == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    else:
        result = num1 / num2
        return result

# Example usage
try:
    print(divide_numbers(10, 2))  # Output: 5.0
    print(divide_numbers(5, 0))   # Raises ZeroDivisionError
except ZeroDivisionError:
    print("Error: Division by zero is not allowed")
```
# Question 2
#### Create a function that checks if a given string is a palindrome. Raise a custom PalindromeError if the input is not a valid string.

```python 
class PalindromeError(Exception):
    pass

def is_palindrome(input_str):
    if not isinstance(input_str, str):
        raise PalindromeError("Input must be a string")

    # Remove spaces and convert to lowercase
    clean_str = input_str.replace(" ", "").lower()

    # Check if the string is equal to its reverse
    if clean_str == clean_str[::-1]:
        return True
    else:
        return False

# Example usage
try:
    print(is_palindrome("racecar"))  # Output: True
    print(is_palindrome("A man a plan a canal Panama"))  # Output: True
    print(is_palindrome(123))  # Raises PalindromeError
except PalindromeError as e:
    print(e)
```
# Question 3
#### Write a Python script that iterates through a list of integers and attempts to divide each integer by zero. Handle the ZeroDivisionError exception within a try-except block, and use a finally block to print a message indicating the end of the iteration process.
```python
numbers = [10, 0, 5, 20, 3]

for num in numbers:
    try:
        result = num / 0
        print(f"{num} / 0 = {result}")
    except ZeroDivisionError:
        print(f"Error: Cannot divide {num} by zero")
    finally:
        print("Iteration completed")
        print("-----------------------")

print("End of script")
```