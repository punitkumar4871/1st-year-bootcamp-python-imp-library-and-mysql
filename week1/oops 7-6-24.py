# Object-Oriented Programming (OOP)

## Benefits:
1. Very efficient in real-life applications.
2. You can create your own data types focused on their specific features, unlike built-in types with predefined properties.

## Core Concepts of OOP:
1. Class
2. Object
3. Abstraction
4. Inheritance
5. Polymorphism
6. Encapsulation

## Class
In Python, a data type is a class. For example, a list is an object and its functions like `append`, `index`, `len` are methods defined in a class. Someone defined those functions in a list class, which is why we can use functions like `append` only on list objects.

## Object Naming
Object names should be in PascalCase (i.e., the first letter should be capitalized).

## Class Example
A class has data (attributes or properties) and methods (functions) in it, which are in snake_case (i.e., using underscores).

```python
class Car:
    color = "blue"  # data
    model = "sports"
    
    def calculate_avg(self, km, time):  # method
        # some code
```

## Object
An object is an instance of a class.

### Methods vs Functions
- `len(l)`: This is a normal function called on a list.
- `l.append()`: This is a method which is defined in the list class, so it is called on list objects.

### Example of a Class
```python
class Atm:
    def __init__(self):  # __init__ is a constructor
        self.pin = ""  # these are variables
        self.balance = 0
        self.menu()  # calling a method
    
    def menu(self):
        user_input = input("Hello, how would you like to proceed?\n1. Enter 1 to create pin\n2. Enter 2 to deposit\n3. Enter 3 to withdraw\n4. Enter 4 to check balance\n5. Enter 5 to exit")
        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.deposit()
        elif user_input == "3":
            self.withdraw()
        elif user_input == "4":
            self.check_balance()
        else:
            print("Exit")
    
    def create_pin(self):
        self.pin = input("Enter your pin")
        print("Pin set successfully")
    
    def deposit(self):
        temp = input("Enter your pin")
        if temp == self.pin:
            amount = int(input("Enter amount to be deposited"))
            self.balance += amount
            print("Deposit successful")
    
    def withdraw(self):
        temp = input("Enter your pin")
        if temp == self.pin:
            amount = int(input("Enter amount to be withdrawn"))
            if amount < self.balance:
                self.balance -= amount
                print("Withdrawal successful")
            else:
                print("Invalid pin")
    
    def check_balance(self):
        temp = input("Enter your pin")
        if temp == self.pin:
            print(self.balance)
        else:
            print("Invalid pin")
```

### Constructor
Constructors are special methods (also called magic methods) that automatically execute when an object is created. Constructors contain variables that should be in the user's hand.

### Example of a Fraction Class
```python
class Fraction:
    def __init__(self, n, d):
        self.num = n
        self.den = d
    
    def __str__(self):
        return "{}/{}".format(self.num, self.den)
    
    def __add__(self, other):
        temp_num = self.num * other.den + other.num * self.den
        temp_den = self.den * other.den
        return "{},{}".format(temp_num, temp_den)
    
    def __sub__(self, other):
        temp_num = self.num * other.den - other.num * self.den
        temp_den = self.den * other.den
        return "{},{}".format(temp_num, temp_den)
    
    def __mul__(self, other):
        temp_num = self.num * other.num
        temp_den = self.den * other.den
        return "{},{}".format(temp_num, temp_den)
    
    def __truediv__(self, other):
        temp_num = self.num * other.den
        temp_den = self.den * other.den
        return "{},{}".format(temp_num, temp_den)
```

## Encapsulation
Encapsulation is the principle of bundling data and methods within a single unit (class). It hides the internal implementation details of an object from the outside world, providing a well-defined interface to interact with the object.

### Instance Variables
Instance variables are variables created inside the `__init__` method and their values are different for different objects. To hide instance variables, we use double underscores `__` before the variable name.

```python
class Atm:
    def __init__(self):
        self.__pin = ""
        self.__balance = 0
        self.menu()
    
    def menu(self):
        user_input = input("Hello, how would you like to proceed?\n1. Enter 1 to create pin\n2. Enter 2 to deposit\n3. Enter 3 to withdraw\n4. Enter 4 to check balance\n5. Enter 5 to exit")
        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.deposit()
        elif user_input == "3":
            self.withdraw()
        elif user_input == "4":
            self.check_balance()
        else:
            print("Exit")
    
    def create_pin(self):
        self.__pin = input("Enter your pin")
        print("Pin set successfully")
    
    def deposit(self):
        temp = input("Enter your pin")
        if temp == self.__pin:
            amount = int(input("Enter amount to be deposited"))
            self.__balance += amount
            print("Deposit successful")
    
    def withdraw(self):
        temp = input("Enter your pin")
        if temp == self.__pin:
            amount = int(input("Enter amount to be withdrawn"))
            if amount < self.__balance:
                self.__balance -= amount
                print("Withdrawal successful")
            else:
                print("Invalid pin")
    
    def check_balance(self):
        temp = input("Enter your pin")
        if temp == self.__pin:
            print(self.__balance)
        else:
            print("Invalid pin")
```

### Reference Variables
While creating an object, the variable used is called a reference variable.

### Passing Objects
Objects can be passed from one function to another.

```python
class Customer:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

def greet(customer):
    if customer.gender == "male":
        print("Hello", customer.name, "sir")
    else:
        print("Hello", customer.name, "ma'am")

cust = Customer("Ankita", "female")
greet(cust)
```

### Collection of Objects
Objects can be collected in a list or other collection types.

```python
class Customer:
    def __init__(self, name, age):
        self.name = name
        self.age = age

c1 = Customer('Nitish', 34)
c2 = Customer('Ankita', 45)
c3 = Customer('Punit', 19)

l = [c1, c2, c3]
for i in l:
    print(i.name, i.age)
```

## Data Abstraction
Abstraction is the principle of exposing only the essential features of an object to the outside world while hiding the unnecessary implementation details.

```python
class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self, new_salary):
        if new_salary > 0:
            self.__salary = new_salary
        else:
            print("Invalid salary")

employee = Employee("John", 30, 5000)
print(employee.get_salary())  # Output: 5000
employee.set_salary(6000)
print(employee.get_salary())  # Output: 6000
```

## Data Hiding
Data hiding is a technique used to prevent direct access to an object's internal data from outside the class.

```python
class MyClass:
    def __init__(self):
        self.__hidden_var = 0

    def get_hidden_var(self):
        return self.__hidden_var

    def set_hidden_var(self, value):
        self.__hidden_var = value

obj = MyClass()
obj.set_hidden_var(10)
print(obj.get_hidden_var())  # Output: 10
```

## Static Variables and Methods
Static variables and methods belong to the class rather than any object instance.

```python
class Atm:
    counter = 1

    def __init__(self):
        self.pin = ""
        self.balance = 0
        self.sno = Atm.counter
        Atm.counter += 1
        self.menu()

    def menu(self):
        user_input = input("Hello, how would you like to proceed?\n1. Enter 1 to create pin\n2. Enter 2 to deposit\n3. Enter 3 to withdraw\n4. Enter 4 to check balance\n5. Enter 5 to exit")
        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.deposit()
        elif user_input == "3":
            self.withdraw()
        elif user_input == "4":
            self.check_balance()
        else:
            print("

Exit")

    def create_pin(self):
        self.pin = input("Enter your pin")
        print("Pin set successfully")

    def deposit(self):
        temp = input("Enter your pin")
        if temp == self.pin:
            amount = int(input("Enter amount to be deposited"))
            self.balance += amount
            print("Deposit successful")

    def withdraw(self):
        temp = input("Enter your pin")
        if temp == self.pin:
            amount = int(input("Enter amount to be withdrawn"))
            if amount < self.balance:
                self.balance -= amount
                print("Withdrawal successful")
            else:
                print("Invalid pin")

    def check_balance(self):
        temp = input("Enter your pin")
        if temp == self.pin:
            print(self.balance)
        else:
            print("Invalid pin")

atm1 = Atm()
print(atm1.sno)  # Output: 1
atm2 = Atm()
print(atm2.sno)  # Output: 2
```

## Static Methods
Static methods are methods that belong to the class rather than any object instance and do not require an instance of the class to be called.

```python
class MathOperations:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def subtract(x, y):
        return x - y

result1 = MathOperations.add(5, 3)
result2 = MathOperations.subtract(10, 4)
print(result1)  # Output: 8
print(result2)  # Output: 6
```

## Instance Methods
Instance methods are methods that operate on an instance of the class and have access to the instance's data.

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} is barking."

dog1 = Dog("Buddy", 3)
print(dog1.bark())  # Output: Buddy is barking.
```

## Class Methods
Class methods are methods that belong to the class and have access to the class data but not instance data.

```python
class Dog:
    species = "Canis lupus familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def get_species(cls):
        return cls.species

print(Dog.get_species())  # Output: Canis lupus familiaris
```
