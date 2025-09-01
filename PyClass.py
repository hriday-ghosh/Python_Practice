
"""

class Person:
    name = "Hriday"
    job = "SDE"


def info(self):
    print(f"{self.name}, is {self.job}")


a = Person()

a.info()


Class is like a Blue Print. 

class Person:
    name = "Hriday"
    job = "SDE"

    def info(self):
        print(f"{self.name}, is {self.job}")


a = Person()
a.info()


Class will be started with a "class" keyword, and this key word will be built as Data Type. 

Now, here Variable will be built when self will be added in front of the Keyword. 

    Here, Function/Method will be built when self will be add within the ()

Difference Between Function and Method? 

Function written in Outside of the class and Method is written in in the Class. 
In Function -> self is not written in the () and in Method self keyword is written in the ().

__init__ = if we write __init__, then we you do not need to call it manually, it will be called automatically. __init__ is a constructor.

"""

"""

class Student:
    def __init__(Self):  # Self is written in the (), so it is a Method
        self.name = input('Enter student name: ')  # This is a variable
        self.roll = input('Enter Roll name: ')
        self.percentage = input("Enter Student Percentage: ")

    def display(self):
        print("Name: ", self.name)
        print("Roll No. ", self.roll)
        print("Percentage: ", self.percentage)


a = Student()  # This is an object
a.display()


"""


"""
Class Concept: 

Car is a Object
So, Car's color, price, model, manufacturer , capacity are can be Properties 
and we can drive the car is Functanalitis 

* Each Object has A) Properties and B) Functanalities

In the programming, 

Properties of Object --> attributes, instance varaible
functanility of object --> methods/function()


    
Example: Robots
A. Name, Model is properties
B. What the Robot can do means Functanility. 


Class is Blue print or code template for object creation. 




# A Sample class with init method
class Person:

    # init method or constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Sample Method
    def say_hi(self):
        print('Hello, my name is', self.name)
        print('Hello, my age is', self.age)


p = Person('Hriday', 25)
p.say_hi()

"-----------------------------------"
p = Person('Gullu', 15)
p.say_hi()
"-----------------------------------"
p = Person('Kallu', 45)
p.say_hi()


# Example:

# Class
class Adder:
    def __init__(self):
        self.total = 0
# Method

    def add(self, num):
        self.total = num+1
# Method 02

    def get_total(self):
        return self.total


# Object
adder = Adder()

num1 = int(input("Enter the first number: "))
adder.add(num1)

num2 = int(input("Enter the second number: "))
adder.add(num2)

print("The total is:", adder.get_total())



#Example_Class: 

class Multiplier:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def multiply(self):
        return self.num1 * self.num2


# create an instance of the Multiplier class, passing in two integers as arguments
multiplier = Multiplier(3, 4)

# call the multiply method on the instance
result = multiplier.multiply()

# print the result
print(result)  # output: 12



"""


# class Robot:
#     def intro_Self(self):
#         print("my name is" + self.name)
#         r1 = Robot()
#         r1.name = "ABC"
#         r1.intro_Self()

#         r2.name = "xyz"
#         r2.introduce_self()


# Example


class car:
    # Wheek = 4 is the class attribute
    # wheel = 4

    def __init__(self, color, week):

        # If we write like, self.color="red", in this case all the object regarding car class will be red but we want color to be specific at every object to the class.
        # self.color = "red"
        self.color = color
        self.week = week

    print("Init is being executed ")


C1 = car("red", "Week52")
C2 = car("Blue", "Week32")

# if we do C1.wheels then the only varibale would be changed, if we want to change the instances for all atribute then work with class and change the instances

car.wheel = 5


print(C1.wheel)
print(C2.wheel)

print(C1.color)
print(C2.color)

print(C1.week)
print(C2.week)


"""
Output:

Init is being executed
5
5
red
Blue
Week52
Week32

"""


# Constructor

# class
class Student:
    # Variable
    roll = ""
    gpa = ""


""" Use of __init__ -> Here we have built constructor __init__ in a Student class, whatever values we put in the object, it will be automaticlally comes into method and value will be set."""


def __init__(self, roll, gpa):
    self.roll = roll
    self.gpa = gpa


def display(self):
    print(f"Roll is {self.roll} and GPA is {self.gpa}")

    rahim = Student(101, 3.47)
    rahim.display()

    # Finding Odd Numbers by a function

    def oddNumbers(start, end):
    """Prints all odd numbers between two integers"""
    for num in range(start, end+1):
        if num % 2 != 0:
            print(num)


oddNumbers(2, 10)


# Finding Odd Numbers by a Class
class OddNumberPrinter:
    """A class that prints all odd numbers between two integers"""

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_odd_numbers(self):
        """Prints all odd numbers between start and end"""
        for num in range(self.start, self.end+1):
            if num % 2 != 0:
                print(num)


printer = OddNumberPrinter(3, 10)
printer.print_odd_numbers()


Python Classes — explained simply (layman language + examples)

Think of a class as a blueprint (like the blueprint for a house).
An object (or instance) is the actual house built from that blueprint.

You use classes when you want to group data (attributes) and behavior (methods) together into a single unit that models a real-world thing.


---

1) Basic class — the anatomy

class Person:                    # 1. class name (blueprint)
    def __init__(self, name, age):  # 2. constructor — runs when you create an object
        self.name = name          # 3. instance attribute
        self.age = age

    def greet(self):              # 4. instance method (needs `self`)
        print(f"Hi, I'm {self.name}, {self.age} years old.")

class Person: — defines a blueprint called Person.

def __init__(self, ...) — special method called automatically when you create an object. It initializes the object.

self — the object being created (like “this house”). Always first parameter of instance methods.

self.name = name — stores the value on the object.


Create and use:

p = Person("Hriday", 28)   # instantiate object
p.greet()                  # calls method -> Hi, I'm Hriday, 28 years old.


---

2) Instance variables vs Class variables

class Car:
    wheels = 4            # class variable (same for all cars)

    def __init__(self, color):
        self.color = color  # instance variable (different per car)

wheels belongs to the class — shared by all instances.

self.color belongs to each object separately.



---

3) Types of methods

Instance method — takes self and works with that object's data.

Class method — takes cls, works with class-level data. Use @classmethod.

Static method — no self or cls, just a function inside the class. Use @staticmethod.


Examples:

class Counter:
    total = 0

    def __init__(self):
        Counter.total += 1

    @classmethod
    def how_many(cls):
        return cls.total

    @staticmethod
    def info():
        print("This class counts instances.")


---

4) Properties — controlled access (getter/setter)

class BankAccount:
    def __init__(self, balance):
        self._balance = balance   # underscore = "internal" convention

    @property
    def balance(self):            # getter
        return self._balance

    @balance.setter
    def balance(self, value):     # setter with validation
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = value

Use @property so acc.balance looks like a normal attribute but runs code behind the scenes.



---

5) Encapsulation (privacy conventions)

_single_leading_underscore → convention: “internal use, don’t touch”.

__double_leading_underscore → name-mangles to reduce accidental access (not true security).



---

6) Inheritance — reuse and extend

class Employee(Person):         # Employee inherits from Person
    def __init__(self, name, age, role):
        super().__init__(name, age)   # call parent constructor
        self.role = role

    def greet(self):             # override greet
        print(f"Hi, I'm {self.name}, {self.role}.")

super() calls the parent class behavior.

Child class can override methods (change behavior) or add new ones.



---

7) Polymorphism — same interface, different behavior

Two different classes implement the same method name:

class Bot:
    def work(self): print("Bot does tasks")

class Human:
    def work(self): print("Human does tasks")

for worker in [Bot(), Human()]:
    worker.work()   # both respond to .work() differently

You can write code that calls .work() without caring about the underlying type.


---

8) Magic / dunder methods — make objects act like built-ins

__str__ → string for users (print)

__repr__ → string for developers (debug)

__len__, __add__, __eq__, etc. — lets your object behave like a list, number, etc.


Example:

class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __repr__(self):
        return f"Point({self.x},{self.y})"

p = Point(2,3)
print(p)   # uses __repr__ or __str__


---

9) Composition vs Inheritance

Inheritance = "is-a" relationship (Employee is-a Person).

Composition = "has-a" relationship (Team has Agents).


Prefer composition when you want to combine behaviors instead of forcing an "is-a" relationship.


---

10) Dataclasses — shorthand for simple classes

from dataclasses import dataclass

@dataclass
class Agent:
    name: str
    level: int

@dataclass auto-generates __init__, __repr__, __eq__ — great for clean models.


---

11) When to use classes vs functions

Use functions for small one-off behaviors (pure tasks).

Use classes when you have grouped data + behavior, need to manage state, or model real-world entities.



---

12) WFM-related examples (practical)

Agent class (scheduling / capacity)

class Agent:
    def __init__(self, name, shrinkage_pct, aht_seconds):
        self.name = name
        self.shrinkage = shrinkage_pct / 100.0  # 0.25 for 25%
        self.aht = aht_seconds                  # average handle time in seconds

    def available_seconds_per_day(self, work_hours=8):
        total = work_hours * 3600               # seconds in day
        return total * (1 - self.shrinkage)

    def handles_calls(self, work_hours=8):
        return self.available_seconds_per_day(work_hours) / self.aht

Use:

a = Agent("Rina", shrinkage_pct=25, aht_seconds=300)
print(a.handles_calls())   # how many calls one agent can handle in a day

Forecast validator (with error handling + dataclass)

from dataclasses import dataclass

@dataclass
class Forecast:
    date: str
    calls: int

    def validate(self):
        if self.calls < 0:
            raise ValueError("Forecast calls cannot be negative")


---

13) Quick cheat-sheet (syntax reminders)

Define class: class Name:

Constructor: def __init__(self, ...):

Instance method: def method(self, ...):

Class method: @classmethod def cm(cls, ...):

Static method: @staticmethod def sm(...):

Property: @property and @x.setter

Inherit: class Child(Parent):

Call parent: super().__init__(...)



---

Final tips (layman style)

Start with simple classes — model one thing (Agent, Forecast, Schedule).

Keep responsibilities single: one class = one job.

Use methods to do things and attributes to store things.

Use @dataclass for simple data containers — saves typing.

Prefer composition to deep inheritance trees — simpler and easier to maintain.



---

