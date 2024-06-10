# Q1.Accessing individual elements
fruits = ["apple", "banana", "cherry"]
first_fruit = fruits[0]  # Accesses "apple"
last_fruit = fruits[-1]  # Accesses "cherry" (negative indexing starts from the end)
     

# Q2.Extracting a sublist:
numbers = [1, 2, 3, 4, 5]
sublist1 = numbers[1:4]  # Extracts [2, 3, 4] (includes index 1, excludes 4)
sublist2 = numbers[2:]  # Extracts [3, 4, 5] (from index 2 to the end)
     

# Q3.Copying a list
original_list = [6, 7, 8]
copy_list = original_list[:]  # Creates a shallow copy
     

# Q4.Reversing a list:
letters = ['a', 'b', 'c', 'd']
reversed_letters = letters[::-1]  # Extracts [d, c, b, a]
     

# Q5.Counting occurrences in a string
message = "Hello, world! How is your day?"
count_of_o = message.count('o')  # Case-sensitive counting
print(count_of_o)  # Output: 2

# Q6.Counting the occurrences of 2
numbers = [1, 2, 2, 3, 1, 4, 2]
count_of_2 = numbers.count(2)
print(count_of_2)
     

# Q7.returns the length
numbers_list = [1, 2, 3, 4, 5]
numbers_tuple = (6, 7, 8, 9)

list_length = len(numbers_list)
tuple_length = len(numbers_tuple)

print("Length of list:", list_length)  # Output: 5
print("Length of tuple:", tuple_length)  # Output: 4
     

# Q8.returns the smallest element in the sequence.
fruits_list = ["apple", "banana", "cherry"]
fruits_tuple = ("mango", "kiwi", "grape")

smallest_fruit_list = min(fruits_list)
smallest_fruit_tuple = min(fruits_tuple)

print("Smallest fruit in list:", smallest_fruit_list)  # Output: apple
print("Smallest fruit in tuple:", smallest_fruit_tuple)  # Output: grape
     

# Q9.This function returns the largest element in the sequence.
numbers_list = [1, 5, 2, 8]
numbers_tuple = (3, 7, 9, 0)

largest_number_list = max(numbers_list)
largest_number_tuple = max(numbers_tuple)

print("Largest number in list:", largest_number_list)  # Output: 8
print("Largest number in tuple:", largest_number_tuple)  # Output: 9
     

# Q10.This method sorts the elements of the list in-place
mixed_list = ["apple", 3, 9.5, True]

mixed_list.sort()  # Sorts the list in-place

print("Sorted list:", mixed_list)  # Output: [3, 9.5, True, apple] (depending on Python version)
     

# Q11. This function calculates the sum of all the elements in the sequence (assumes numeric data)
numbers_list = [4, 7, 2, 11]
numbers_tuple = (6, 3, 8, 1)

list_sum = sum(numbers_list)
tuple_sum = sum(numbers_tuple)

print("Sum of list elements:", list_sum)  # Output: 24
print("Sum of tuple elements:", tuple_sum)  # Output: 18
     