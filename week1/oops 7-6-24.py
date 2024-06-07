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
    
























