'''oops:-object oriented programmig
benefit :-1.) very efficient in real life application
2.)u can make your own data types which will focus on their own feature not like built i which have some specific properties

'''
#core concept of oops:-
'''1.class
2.object
3.abstaration
4.inheritance
5.polymorphism
6.encapsulation'''

# class
'''in python data type is class
ex:- a list is object and its function like append,index,len are function defined in class someone made those funcn in a class of list thats why we can use functioon like append,etc on list object only'''

# object name should be in pascal case i.e first letter should be capital 
# class has data(attribute of class (properties)) and methods(funcn) in it which are in snake case i.e _ this should be used
'''example of a class
     class Car:
        color="blue" #data
        model="sports
        def calculate_avg(km,time): #method
            #some code'''


#object:- object is instance of a class

#Note:- method are function which are called in a class
'''difference b/w method and function are :-
1:-len(l):-this is a normal function called on a list
2:-l.append():-this is method which is determined on list class so it is coming aterwards
note2:- function are available to all class and object whereas methods are avialble for that specific class object only
eg:- of a class:-'''
class Atm:
    def __init__(self):   #init is a constructor:special method  jiske andar ka code automatically executive when u make class
        self.pin="" # these are variable
        self.balance=0
        self.menu()  # callinf for mathod 
    def menu(self):
        user_input=input("hello how would u like to proceed?\n1.enter 1 to create pin \n 2. enter 2 to deposit \n 3.) enter 3 to withdraw \n 4. enter 4 to chekc balance \n 5. enter 5 to exit")
        if user_input=="1":
            self.create_pin()
        elif user_input=="2":
            self.deposit()
        elif user_input=="3":
            self.withdraw()
        elif user_input=="4":
            self.check_balance()
        else:
            print("Exit")
    def create_pin(self):
        self.pin=input("enter your pin")
        print("pin set succesfully")
    def deposit(self):
        temp=input("enter your pin")
        if temp==self.pin:
            amount=int(input("enter amount to be deposited"))
            self.balance=self.balance + amount
            print("deposit successfull")
    def withdraw(self):
        temp=input("enter your pin")
        if temp==self.pin:
            amount=int(input("enter amoun tot be withdrawn"))
            if amount<self.balance:
                self.balance=self.balance-amount
                print("withdraw succesfull")
            else:
                print("invalid pin")
    def check_balance(self):
        temp=input("enter your pin")
        if temp == self.pin:
            print(self.balance)
        else:
            print("invalid pin")

# adavantage :- each object which we will make can have their own value i.e their own instance eg. if we make sbi=atm() and hdfc=atm() then we add 25000 in sbi(sbi.deposit()) and 5000 in hdfc(hdfc.deposit()) then if we check balance then their values will be differnec for each object
# constructore ar especial method , magic method which automatiically called or trigeer itself when object is called
# i.e constructor contain those variable in it which should be in hand of user or jo khud karna ha like app open hote hi
# in oops one method of same class cannot access another method of that class therfore we use self (object) to act like a connection b/w them
# we can see in above code that init want access of menu and menu want access of method below it we cannot connet them without self.

'''example 2:- we will create a class i.e a new data strucutre which can handle fraction without converting it in decimal'''


# def __str__ :_ return string it transport to this point 


class Fraction:
    def __init__(self,n,d):
        self.num=n
        self.den=d
    def __str__(self):
        return "{}/{}".format(self.n,self.d)
    # now we will add sub methd in i now it cannot add bcz we havent mention how to add. we can unserstand it by set like its a class where add method is also not there therfore wecant add set
   
     
     # __add__ :- when we add (use +) it take us to add consructor
    
     
    def __add__(self,other): 
        temp_num=self.num* other.den +other.num*self.den
        temp_den=self.den * other.den
        return "{},{}".format(temp_num,temp_den)
    def __sub__(self,other): 
        temp_num=self.num* other.den -other.num*self.den
        temp_den=self.den * other.den
        return "{},{}".format(temp_num,temp_den)
    def __mul__(self,other): 
        temp_num=self.num * other.num
        temp_den=self.den * other.den
        return "{},{}".format(temp_num,temp_den)
    def __truediv__(self,other): 
        temp_num=self.num* other.den 
        temp_den=self.den * other.den
        return "{},{}".format(temp_num,temp_den)




# encapsulation


# encapsulation:- 
# Encapsulation is the principle of bundling data and methods within a single unit (class). It helps in hiding the internal implementation details of an object from the outside world, providing a well-defined interface to interact with the object.
# # instance variale :- variable which are made inside init class are known as insatnce varibale
# there valuw are different for different object
# one disadvantage of code whihc we made earlier was like we can check balance by instance variable i.e we can check by
''' spi.balance which will show our balance without our pin ideally w should do sbi.check_balance '''
''' same with pin also he can chekc our pin'''
# so for this we use __ before our instance variable
class Atm:
    def __init__(self):   #init is a constructor:special method  jiske andar ka code automatically executive when u make class
        self.__pin="" # these are variable
        self.__balance=0
        self.menu()  # callinf for mathod 
    def menu(self):
        user_input=input("hello how would u like to proceed?\n1.enter 1 to create pin \n 2. enter 2 to deposit \n 3.) enter 3 to withdraw \n 4. enter 4 to chekc balance \n 5. enter 5 to exit")
        if user_input=="1":
            self.create_pin()
        elif user_input=="2":
            self.deposit()
        elif user_input=="3":
            self.withdraw()
        elif user_input=="4":
            self.check_balance()
        else:
            print("Exit")
    def create_pin(self):
        self.__pin=input("enter your pin")
        print("pin set succesfully")
    def deposit(self):
        temp=input("enter your pin")
        if temp==self.__pin:
            amount=int(input("enter amount to be deposited"))
            self.__balance=self.__balance + amount
            print("deposit successfull")
    def withdraw(self):
        temp=input("enter your pin")
        if temp==self.__pin:
            amount=int(input("enter amoun tot be withdrawn"))
            if amount<self.__balance:
                self.__balance=self.__balance-amount
                print("withdraw succesfull")
            else:
                print("invalid pin")
    def check_balance(self):
        temp=input("enter your pin")
        if temp == self.__pin:
            print(self.__balance)
        else:
            print("invalid pin")
"""now we cannot access our data with data memeber"""
# this hides our our data member but in python nothing is properly private 
# our balance is not properly hiden just it save out data lile _Atm__balance therfefore if anyone know your data member name and class name then he can access your data
''' but still if we want that someone can change and see our thng then we can use
1.) get 
2.)set '''
''' this is made for emergency that if u wan tot chekc in emergency u can check it u can also change it but using my logic'''

'''this all things combining is called encapsulation'''



# refernce variable:-
# while creating object the variable whihc is used is called as reference variable. i.e in above code hdfc or sbi can be reference variable


# pass by refernce 


# this state the we can pass object form one function to other
#eg:-
class Customer :
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender

def greet(customer):
    if customer.gender=="male":
        print("hello",customer.name,"sir")
    else:
        print("hello",customer.name,"maam")
cust=Customer("ankita","female")
greet(cust)


# here both customer and cust toward same point therfore their ids are also same
# in mutable object classes are also mutable address remain same after insertio or some changes and in immutable addresses changes




# collection of objects
# we can collect object in oops
#ex:-

class Customer:
    def __init__(self,name,age):
        self.name=name
        self.age=age
c1=Customer('nitish',34)
c2=Customer('ankita',45)
c3=Customer('punit',19)

l=[c1,c2,c3]
for i in l:
    print(i.name,i.age)




#Data Abstraction
'''Abstraction is the principle of exposing only the essential features of an object to the outside world while hiding the unnecessary implementation details.
'''
class Employee:
    def __init__(self, name, age, salary):
        # Public attributes
        self.name = name
        self.age = age
        
        # Private attribute
        self.__salary = salary

    def get_salary(self):
        # Method to retrieve the salary
        return self.__salary

    def set_salary(self, new_salary):
        # Method to update the salary
        if new_salary > 0:
            self.__salary = new_salary
        else:
            print("Invalid salary")

# Create an instance of the Employee class
employee = Employee("John", 30, 5000)

# Retrieve the salary using the get_salary method
print(employee.get_salary())  # Output: 5000
# Update the salary using the set_salary method
employee.set_salary(6000)

# Retrieve the updated salary
print(employee.get_salary())  # Output: 6000





# Data Hiding
'''Data hiding is a technique used to prevent direct access to an object's internal data from outside the class
   ''' 
# we use hidden var in it
class MyClass:
    def __init__(self):
         self.__hidden_var = 0  # Hidden variable, initialized with 0

    def get_hidden_var(self):
         return self.__hidden_var  # Returns the value of the hidden variable

    def set_hidden_var(self, value):
         self.__hidden_var = value  # Updates the hidden variable with the provided value
obj = MyClass()
obj.set_hidden_var(10)  # Sets the hidden variable to 10
print(obj.get_hidden_var())  # Output: 10



#static variable and methods;-


# as we have studied that each object have its own valuei.e instances but sometime we need staic variable i.e they should affect each other i.e if we are counting something 
#efg:- degree static and cgpa:- instant
#NOte:_ static veriable is created before contructor and instant are created undere constructor

class Atm:
    #static
    counter=1
    def __init__(self):   #init is a constructor:special method  jiske andar ka code automatically executive when u make class
        self.pin="" # these are variable
        self.balance=0
        self.sno=Atm.counter+1
        Atm.counter=Atm.counter+1
        self.menu()# callinf for mathod

    def menu(self):
        user_input=input("hello how would u like to proceed?\n1.enter 1 to create pin \n 2. enter 2 to deposit \n 3.) enter 3 to withdraw \n 4. enter 4 to chekc balance \n 5. enter 5 to exit")
        if user_input=="1":
            self.create_pin()
        elif user_input=="2":
            self.deposit()
        elif user_input=="3":
            self.withdraw()
        elif user_input=="4":
            self.check_balance()
        else:
            print("Exit")
    def create_pin(self):
        self.pin=input("enter your pin")
        print("pin set succesfully")
    def deposit(self):
        temp=input("enter your pin")
        if temp==self.pin:
            amount=int(input("enter amount to be deposited"))
            self.balance=self.balance + amount
            print("deposit successfull")
    def withdraw(self):
        temp=input("enter your pin")
        if temp==self.pin:
            amount=int(input("enter amoun tot be withdrawn"))
            if amount<self.balance:
                self.balance=self.balance-amount
                print("withdraw succesfull")
            else:
                print("invalid pin")
    def check_balance(self):
        temp=input("enter your pin")
        if temp == self.pin:
            print(self.balance)
        else:
            print("invalid pin")
c1=Atm()
c2=Atm()
c3=Atm()
c1.sno  #1

c2.sno #2
c3.sno #3



#inheritance:-
'''nheritance is a fundamental concept in object-oriented programming (OOP) that allows a class (known as a subclass or derived class) to inherit properties and behaviors 
(methods) from another class (known as a superclass or base class)This mechanism promotes code reusability and establishes a natural hierarchy between classes.'''
     
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."
class Dog(Animal):
    def speak(self):
        return f"{self.name} barks."
class Cat(Animal):
    def speak(self):
        return f"{self.name} meows."
dog = Dog("Buddy")
cat = Cat("Whiskers")
print(dog.speak())  
print(cat.speak()) 



#polymorphism:-
'''polymorphism is a core concept in object-oriented programming (OOP) that allows objects of different classes to be treated as objects of a common superclassIt provides a way to perform a single action in different forms. 
Polymorphism enhances the flexibility and maintainability of the code by enabling a single interface to represent different underlying forms (data types)'''

class Animal:
    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Dog(Animal):
    def speak(self):
        return "Bark"
class Cat(Animal):
    def speak(self):
        return "Meow"
class Bird(Animal):
    def speak(self):
        return "Chirp"
def make_animal_speak(animal):
    print(animal.speak())
dog = Dog()
cat = Cat()
bird = Bird()
make_animal_speak(dog)  
make_animal_speak(cat)  
make_animal_speak(bird)




#decorators:-
'''Decorators in object-oriented programming (OOP) are a design pattern that allows behavior to be added to individual objects, dynamically, without affecting 
the behavior of other objects from the same class. In Python, decorators are a powerful and expressive way to modify or extend the behavior of functions or methods.'''
import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds to execute.")
        return result
    return wrapper
@timing_decorator
def example_function():
    time.sleep(2)
    print("Function execution completed.")
example_function()



# generators
''' generators are a specific type of iterator, implemented using the yield keyword in Python.They allow for the creation of iterators in a simpler
and more memory-efficient way compared to traditional iterators'''
#-eg- print fibo series:-
def fibonacci_generator(limit):
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b
for num in fibonacci_generator(10):
    print(num)


# Method overloading

#Method overloading is a feature in some programming languages that allows a class to have multiple methods with the same name but different parameter lists

























