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

If you want, I can:

Give a complete runnable WFM script (agents + forecast + capacity checker), or

Convert this into a one-page PDF cheat-sheet for quick reference.


Which one should I make right now?

