# Inheritance means -> Using existing code'feature.

# Phone is a Parent Class or Super Class.
class phone:
    def call(self):
        print("You can call Phone class")

    def message(self):
        print("You can message/Phone Class")

# Apple is child Class Or Sub Class


class Apple(phone):
    # After putting phone into the () we can use phone's class call and message method
    def photo(self):
        print("You can click photo")


# Object
p = phone()
p.message()
p.call()


"""
What is multiple inheritance?
Ans-> Inheritance which contain move classess and only one parent class is called as Multiple Inheritance.

Class Parent_1():
    Properties
Class Parent_2()"
    Properties
Class Child(Parent_1,Parent_2):
    Properties        
"""

"""
Example: Like we have a team leader who need to build a Dynamic Website and he has 2 team member named Ram and Chutki, so, Ram will build Backend and Chutki will build Frontend.

"""


class Ram:
    Back = "Oracale and Python"

    def BackEnd(self):
        print("Backend is implimented using", self.Back)


class Chutki:
    Front = "HTML, CSS, JS"

    def FrontEnd(self):
        print("Front end is implimented using", self.Front)

# TeamLead Class


class TeamLead(Ram, Chutki):
    def show(self):
        print("Dynamic Web done by Ram and Chutki")


Team = TeamLead
Team.BackEnd()
Team.FrontEnd()
Team.show()


"""
Syntax:

class Father: #Parent Class 
    members/Function of class Father()
class Mother: #Parent Class
    members/Function of class Mother()
class Son(Father, Mother): #Child Class which can access Parent class properties and Function
    members/Function of class Son()

"""

# Simple Example:


class Father:
    def show_Father(self):
        print("Father Class Method")


class Mother:
    def show_Mother(self):
        print("Mother Class Method")


class Son(Father, Mother):
    def show_Son(self):
        print("Son's Class Method")


S = Son()
S.show_Son()
S.show_Father()
S.show_Mother()


# Example With __init__:

class Father:
    def __init__(self):
        print("Father class constructor")

    def show_Father(self):
        print("Father Class Method")


class Mother:
    def show_Mother(self):
        print("Mother Class Method")


class Son(Father, Mother):
    def __init__(self):
        print("Son class constructor")

    def show_Son(self):
        print("Son's Class Method")


S = Son()
S.show_Son()
S.show_Father()
S.show_Mother()


# Example With __init__:

class Father:
    def __init__(self):
        super().__init__()  # Calling Father class Constructor by super().__init__
    print("Father Class Construtor")

    def show_Father(self):
        print("Father Class Method")


class Mother:
    def __init__(self):
        super().__init__()    # Calling Mother class Constructor by super().__init__
    print("This is Mother Construtor")

    def show_Mother(self):
        print("Mother Class Method")


class Son(Father, Mother):
    def __init__(self):
        super().__init__()  # Calling Father class Constructor by super().__init__
        print("Son class constructor __init__")
# After putting super().__init__() method on Father Class, so, Father class will be printed.

    def show_Son(self):
        print("Son's Class Method")


S = Son()
# S.show_Son()
# S.show_Father()
# S.show_Mother()


"""
Output: 
Father Class Construtor
This is Mother Construtor
Son class constructor __init__

"""


"""
Here, our output is "Son class constructor" and we can check that Python ignored Father's __init__ method.
So, here Python only consider Child class Method.
"""
