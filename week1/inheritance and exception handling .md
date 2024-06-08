# class relationships
class relationships is fundamental in objectoriented programming (OOP). Here are the main types of class relationships:
## 1.)inheritance relationship (is-A relationship)
Inheritance is a relationship where a class (subclass or derived class) inherits properties and behavior (methods) from another class (superclass or base class)
#### biggest addvamtage of inheritance is code reusabilty
 u can access feature of one class toanother if uwant some features of it
 a child class inhermit datamember ,constructor and method but remember we cant inherhit hidden private member
# example1:- inheriting class
 ```python
 class User:
    def login(self):
        print("login")
    def register(self):
        print("register")
class Student(User):
    def enroll(self):
        print("enroll")
    def review(self):
        print("review")
# as we passed enroll class into student class so student can access 4 method login,rgister,enroll,review.

stu1=Student()
stu1.enroll()
stu1.review()
stu1.login()
stu1.register()

# but its reverse is not true i.e user cannot access enroll and review.
 ```

# example2:- inherting constructor
```python
class Phone:
    def __init__(self,price,brand,camera):
        print("inseide phone construcotr")
        self.price=price
        self.brand=brand
        self.camera=camera
    def buy(self):
        print("buying a phone")
    def return_phone(self):
        print("returning a ohone")
class Feature_phone(Phone):
    pass
class Smartphone(Phone):
    pass
s=smartPhone(20000,"Apple",13)
# now smart phone have no constructor and we are giving 3 parameter so it will see parameter as differ class is given it will go to that class
#O/p:- inside phone constructor
# concept child class will call parent construtor also.

```

# example 3:- lets check it can access private members also or not:-

```python
class Phone:
    def __init__(self,price,brand,camera):
        print("inseide phone construcotr")
        self.price=price
        self.__brand=brand  # private data member
        self.camera=camera
    def buy(self):
        print("buying a phone")
    def return_phone(self):
        print("returning a ohone")
class Feature_phone(Phone):
    pass
class Smartphone(Phone):
    pass
# s=smartPhone(20000,"Apple",13)
#  print(s.__brand)now this will crash bcz brand is hidden 

```


# example:- 4 polymorphism:-
polymorphism is where a same method is present is differ classes and it functinality is also different 
```python
class Phone:
    def __init__(self,price,brand,camera):
        print("inseide phone construcotr")
        self.price=price
        self.__brand=brand  # private data member
        self.camera=camera
    def buy(self):
        print("buying a phone")
    def return_phone(self):
        print("returning a ohone")

class Smartphone(Phone):
    def buy(self):
        print("buying a smartphone")
s=smartphone(20000,"apple",13)
s.buy()
```
# now as buy is in both classes so questionn is whihc one will be executed so child class method will be executed.
# output will be 
'''inside phone constructor 
buying a smartphone '''
# fist it go to constructor of parent class but buy will be executed of child class
'''this is called method overriding'''










## 2.) Aggregation (Has-A Relationship, but with Ownership)
Aggregation is a special form of association where a class has a reference to another class but does not own the other class. The lifecycle of the referenced object is not managed by the containing class.
for eg:- customer has address here address doesnt own customer
# for example1
```python
class Customer:
    def __init__(self,name,gender,address):
        self.name=name
        self.gender=gender
        self.address=address
class Address:
    def __init__(self,city,pincode,state):
        self.city=city
        self.pincode=pincode
        self.state=state
# we passes object as parameter
# now we will use address class object A parameter of customer but it doesnt own it.
add=Address("kolkata",700156,"wb")
cust=Customer("Nitish","Male",add)
print(cust.address.pincode)
```
# example 2:- it can also call for objects or method of other class for specific work
```python
class Customer:
    def __init__(self,name,gender,address):
        self.name=name
        self.gender=gender
        self.address=address
    def edit_profile(self,new_name,new_city,new_pin,new_state):
        self.name=new_name
        self.address.change_address(new_city,new_pin,new_state)
class Address:
    def __init__(self,city,pincode,state):
        self.city=city
        self.pincode=pincode
        self.state=state
    def change_address(self,new_city,new_pin,new_state):
        self.city=new_city
        self.pincode=new_pin
        self.state=new_state
add=Address("kolkata",700156,"wb")
cust=Customer("Nitish","Male",add)
cust.edit_profile("ankit","gurgaon",122011,"haryana")
print(cust.address.pincode)

```

        

