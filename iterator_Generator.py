
"""Iterator:

We can not iterate integer formula in Python. We can iterate List [], Tuple {}, Dictionary {}

By the help of iterate we can iterate or print the data type sequentially.
"""

L = [1, 2, 3, 4]
IT = iter(L)
print(next(IT))
print(next(IT))

# Here print will be 1,2 as we put print twice.


list02 = [1, 2, 3, "Hriday", True]
# we are iterating the List by the help of iterating function.
ITERATION_List = iter(list02)
# Here, we are trying to print here finally.
# By the help of next() function access the function accordingly.
print(next(ITERATION_List))
print(next(ITERATION_List))
print(next(ITERATION_List))
print(next(ITERATION_List))

# We can do the same thing by using For Loop, advantages of the for loop is, it never shows stoppage error.


# Generator using For Loop:

def gen01():
    print('Hi')
    yield 5

    print('Hello')
    yield 10

    print("Hello Hriday")
    yield 15


# Generator using For Loop
gen_values = gen01()
for i in gen_values:
    print(i)


"""Output:
Hi
5
Hello
10
Hello Hriday
15
"""

"""When we try to use For Loop here instead of next () function then we are not facing IterationStoppage Error.
"""

"""Putting return statment Generator Function
"""


def gen01():
    print('Hi')
    yield 5
# Using Return
    return

    print('Hello')
    yield 10

    print("Hello Hriday")
    yield 15


# Generator using For Loop
gen_values = gen01()
for i in gen_values:
    print(i)

# Outout:
# Hi
# 5


"""
Iterator VS Generator: 

1. Generator are mostly used in loops to generate an iterator by returning all valuess in the loop without affecting the iteration of the loop. 

An iterator is an object which contains a countable number of values and it is used to iterate over iterable objects like list, Tuple, Sets etc. 

2. Generator uses Yeild Keyword and Iterator uses iter() and next functions(). 

3. Every generator is an iterator buy every iterator is not an iterator. 

4. Generators in Python are more memory efficient and Iterator is less memory efficient. 

5. Generators are iterarators which can execute only once and Iterators are used mostly to iterate or convert other objects to an iterator using iter() functions. 
"""


# Generator:

"yeild and return both work as return but when we use yeild statement then the function wont stop process and the another hand if we use normal function then it goes wash away from the memory after calling/using the function."


def Normal_Function(a, b):
    c = a+b
    return c


print(Normal_Function(5, 7))


def Generator_Function():
    print("Hello Hriday")
    yield 5

    print('Hello India')
    yield 15

    print("Hello Bharat")
    yield 20

    gen_values = Generator_Function()
    print(gen_values)

    print(next(gen_values))
    print(next(gen_values))
    print(next(gen_values))


# Gen_Function02


def Gen03(a, b):
    yield a
    yield b


# result = Gen03(15, 20)
# print(result)
