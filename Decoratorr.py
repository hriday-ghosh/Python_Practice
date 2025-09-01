"""
A decorator means wrap a function into another function.


In simple words, a decorator takes in a function adds some functionality and returns it.

map, filter and reduce in Python are decorator in Python.


1st Exapmle:

def increment(x):
    return x+1


def operate(func, x):
    result = func(x)
    return result


print(operate(increment, 3))



2nd Wrapper:


def starline(func):
    def wrapper():
        print("1st line")
        func()
        print("2nd Line")
    return wrapper


@starline
def display():
    print("3rd line")


display()



def decor(fun):
    def inner():
        a = fun()
        add = a+5
        return add
    return inner


def num():
    return 10


result_fun = decor(num)

print(result_fun())

Exammple: 

def decor1(num):
    def inner():
        b = num()
        multi = b*5
        return multi
    return inner


def decor(num):
    def inner():
        a = num()
        add = a+5
        return add


def num():
    return 10


num = decor(decor1(num))
print(num())


"""
import os


def test25(func):
    def test26():
        print("This is Function No.  26")
        end = time.time()
        func()
        print(func())
        print(end-start)
    return test25



Alright 👍 let’s make decorators in Python super easy for you.


---

🟢 What is a Decorator?

Think of a decorator as a wrapper that adds extra power to a function without changing the original function’s code.

👉 In layman’s words:
Imagine you have a simple coffee (your function).

If you add milk + sugar on top, it’s still coffee but “decorated”.

You didn’t change the coffee itself, you just wrapped extra features around it.


That’s exactly what a decorator does in Python.


---

🟢 Example without Decorator

def greet():
    print("Hello, Welcome!")

greet()

Output:

Hello, Welcome!

This is just a plain coffee ☕ (simple function).


---

🟢 Example WITH Decorator

def my_decorator(func):
    def wrapper():
        print("✨ Before the function runs")
        func()
        print("✅ After the function runs")
    return wrapper

@my_decorator
def greet():
    print("Hello, Welcome!")

greet()

Output:

✨ Before the function runs
Hello, Welcome!
✅ After the function runs


---

🔹 Explanation (in easy way):

1. @my_decorator → This line tells Python:
"Before running greet(), wrap it inside my_decorator."


2. wrapper() → Adds extra code before and after the original function.


3. So the decorator decorates the function with extra features.




---

🟢 Real-Life Use Case

Logging (recording function activity)

Authentication (check user before running function)

Measuring execution time


Example: Measuring how long a function takes

import time

def timer_decorator(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print("⏱ Time taken:", end - start, "seconds")
    return wrapper

@timer_decorator
def long_task():
    time.sleep(2)   # pretend it's a heavy task
    print("Task Finished!")

long_task()

Output:

Task Finished!
⏱ Time taken: 2.0 seconds


---

✅ So in layman’s terms:
A decorator = “an extra layer of code” that runs before/after your actual function — like adding milk & sugar to coffee ☕.


---

Do you want me to show you how decorators can be used in real WFM/Data Analyst tasks (like logging forecast runs or timing a scheduling script)?