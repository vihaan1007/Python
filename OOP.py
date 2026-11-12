#OOP: to map with real world scenarios, we started using objects in code. This is called Object Oriented Proggraming
#this is a evolution of function
#we make classes and then object or instance is created on that
#class s a blueprint for objects

class Student:# class keyword and class name
    name = "karan"#attr
s1 = Student()
print(s1)#the objet
print(s1.name)#attr of object from the class
#class is the keyword to make classes
#the class name is the name to a class

#__init__
#__init__ is like parameter it is runned once per object creation
class Car:
    def __init__(self, fullname):# self is necessary. it is the class object
        name = fullname
        print("Object created:" ,name)
car1 = Car("Toyota")

#class attr is common for all object
#object attr is different for each object
#method is for adding a method to the specific class like str or int or float have

class Hello:
    def __init__(self, name):
        self.name = name
    def hello(self):#self is important for all methods. It unlocks all object attr
        return self.name
hello = Hello("ABCD")
print(hello.hello())

#practice1
#Create student class that takes name & marks of three subject as arguments in constructor. Then create a method to print the average
class student:
    def __init__(self, name, phy, chem, bio):
        self.name = name
        self.phy = phy
        self.chem = chem
        self.bio = bio
    def average(self):
        total = self.phy + self.chem + self.bio
        print(total / 3)

s2 = student("Alex", 20, 20, 30)
s2.average()

#static methods
#methods that dosent use the self parameter
class Printhello:
        @staticmethod#decorator
        def hello():
            print("Hello")
stat = Printhello()
stat.hello()

#decorators allow us to wrap another function in order to extend the behaviour of a wrapped function without modifying it.

#THE FOUR PILLARS OF OOP
#abstraction
#encapsulation
#inheritence
#polymorphism

#abstraction means hiding other things and only showing essential to the user. We do it
#encapsulation means the layout of the class like init, methods, class. We do it
#inheritence and polymorphism is for later

#practice1
#Create Account class with 2 attributes - balance and account.no. Create methods for debit, credit & printing the balance

class Account:
    def __init__(self, balance, acc_no):
        self.balance = balance
        self.acc = acc_no
    def debit(self, debit):
        if(self.balance >= debit):
            print("debit is not possible because you dint have enough balance")
        else:
            self.balance -= debit
    def credit(self, credit):
        self.balance += credit
    def balance(self):
        print(self.balance)

#del keyword
#used to delete object properties or object itself
del stat
#stat no longer exists

#Private attributes & methods
#private attr and method are only accesable in the class and are not available from outside
class Password:
    def __init__(self, password):
        self.__password = password#two underscores makes it private

#INHERITENCE: third pillar
#when one class(child/derived) derives the properties from a class(parent/base)
class Parent:
    @staticmethod
    def start():
        print("car started")
    @staticmethod
    def stop():
        print("Car stopped")

class Child(Parent):#inherited
    def __init__(self, name):
        self.name = name

chi = Child("Toyota")
print(chi.name)
chi.start()
chi.stop()

#single inheritence: parent -> child. just did
#multi-level inheritence: grandparent -> parent -> child
#multiple inheritence: parent1, parent2 -> child

#super() method: it is used to access methods of the parent class. super means parent
class Ca:
    def __init__(self, type):
        self.type = type
    @staticmethod
    def start():
        print("Car started")
    @staticmethod
    def stop():
        print("Car stopped")
class Toc(Ca):
    def __init__(self, name, type):
        self.name = name
        self.type = type
        super().__init__(type)
toyc = Toc("prius", "electric")#second only works because of super

#classmethod: they are decorators to access class attr
class Person:
    name = "Anonymous"
    @classmethod
    def changeName(cls, name):
        cls.name = name

person = Person()
person.changeName("Alex")
print(Person.name)

#property decorator: it is a decorator that can turn a function into a property like a attr
class Studenta:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math
    @property
    def percentage(self):
        return str(self.phy + self.chem + self.math / 3) + "%"
percen = Studenta(98, 97, 99)
print(percen.percentage)
percen.phy = 86
print(percen.percentage)#changed

#Fourth pillar of OOP; polymorphism
#when the same operator is allowed to have different meaning according to context
#in +,
#list are merged
#integers and floats are added
#strings are concated

#operator overloading
#operators ad dunder functions
#+ -> a.__add__(b)
#- -> a.__sub__(b)
#* -> a.__mul__(b)
#/ -> a.__truediv__(b)
#% -> a.__mod__(b)

#a complex number class
class Complex:
    def __init__(self, i, j):
        self.i = i
        self.j = j
    def showNumber(self):
        print(self.i, "i + ", self.j, "j", sep = "")
    def __add__(self, num2):
        newreal = self.i + num2.i
        newimg = self.j + num2.j
        return Complex(newreal, newimg)
    def __sub__(self, num2):
        newreal = self.i - num2.i
        newimg = self.j - num2.j
        return Complex(newreal, newimg)
    def __mul__(self, num2):
        newreal = self.i * num2.i
        newimg = self.j * num2.j
        return Complex(newreal, newimg)
    def __truediv__(self, num2):
        newreal = self.i / num2.i
        newimg = self.j / num2.j
        return Complex(newreal, newimg)
    def __mod__(self, num2):
        newreal = self.i % num2.i
        newimg = self.j % num2.j
        return Complex(newreal, newimg)

num1 = Complex(1, 3)
num1.showNumber()

num2 = Complex(2, 6)
num2.showNumber()

num3 = num1 + num2#possible because of the fundeer function of add
num4 = num1 - num2
num5 = num1 * num2
num6 = num1 / num2
num7 = num1 % num2
num3.showNumber()
num4.showNumber()
num5.showNumber()
num6.showNumber()
num7.showNumber()
#practice1
#Define a Circle class to create a cirle with radius r using the constructor. Define an area() method of the class and a perimeter() method of the class.
class Circle:
    def __init__(self, r):
        self.r = r
    def area(self):
        return 3.1415926535897932384626433832795028841971537510 * (self.r ** 2)
    def perimeter(self):
        return 2 * self.r * 3.1415926535897932384626433832795028841971537510

#practice2
#Define a Employee class ...
class Employee:
    def __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary
    def showDetails(self):
        print("Role:", self.role)
        print("department:", self.department)
        print("salary:", self.salary)

class Engineer(Employee):
    def __init__(self, name, age, role, department, salary):
        self.name = name
        self.age = age
        super().__init__(role, department, salary)