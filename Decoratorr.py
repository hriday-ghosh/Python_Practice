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
