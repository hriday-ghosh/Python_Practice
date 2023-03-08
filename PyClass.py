
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

