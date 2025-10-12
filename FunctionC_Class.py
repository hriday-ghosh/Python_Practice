"""
def test1():
    print("Hi this is a Function")
    return ("Hi this is a Function")



def test2():
    return 5


B = test2

print(B)

type(B)

# Writing a python Function of addition 2 nos.

def Hriday(a, b):
    return (a+b)


a = "Kalu"
b = "Lallu"


print(Hriday(a, b))

# * - * - astetic means, you can pass any numbers of input
# and whatever input we provide, it will print in tuple format


def test(*args):
    return args


print(test(1, 3, 4, 5, "Ram"))


# So, here we can do a type casting by putting list as (*args) provides always Tupele.

def test04(*args):
    return list(args)


print(test04(1, 5, 7, 8, "Hriday"))


Another Function:

def test(*args):
    l = []
    for i in args:
        l.append(i)
        return l


print(test(1, 5, 7, 8))



write a Python function which take input as string from the user and output will be number of digits or length on the string

def Hriday_Print():
    a = input("Enter the word: ")
    b = len(a)
    return (b)


# print(Hriday_Print())
C = Hriday_Print()
print(C)


"""


# Write a function which is going to return only Vowels

# A = input("Enter the number: ")
# B = "aeiouAEIOU"
# for i in B:
#     if A == i:
#         print("Vowels are: ")


# n = input("Enter a number: ")
# L = list(n)
# print(L)
# V = ["a", "i"]

# out = []
# for i in L:
#     if i in V:
#         out.append(i)
#         print('Vowels are: ')
#         print(set(out))


# I = input("Enter word: ").lower()
# V = ""
# if V in I:
#     V = + "a"
#     if V != "":
#         print(V)
#     else:
#         print("None")

# i = input("Enter word: ").lower()
# v = ""
# if v in i:
#     v = v + "a"
# if v != "":
#     print(v)
# else:
#     print("None") 


input_string = input("Enter a string: ")
vowels = ""

# Loop through each character in the input string
for char in input_string:
    # Check if the character is a vowel (aeiou)
    if char.lower() in "aeiou":
        # If the character is a vowel, add it to the vowels string
        vowels += char

# Check if any vowels were found in the input string
if len(vowels) > 0:
    # Print the vowels string
    print("The vowels in the string are:", vowels)
else:
    print("There are no vowels in the string.")


Perfect 👍 Let’s go step by step and explain Functions in Python in very easy and layman’s language.


---

🟢 What is a Function in Python?

👉 A function is like a machine or recipe:

You give it inputs (ingredients).

It does some work (cooking).

It gives you an output (final dish).


So instead of writing the same code again and again, you put it inside a function and reuse it whenever you want.


---

🟢 Types of Functions in Python

1. Built-in Functions

These are ready-made machines that Python already gives you.
Examples:

print("Hello")   # prints text
len("Python")    # counts length of string → 6
type(10)         # tells the type → int

👉 You don’t need to create them, just use them.


---

2. User-Defined Functions

These are functions you create yourself.

🔹 Syntax:

def function_name(parameters):
    # code block
    return result   # (optional)

🔹 Example:

def greet(name):
    print("Hello", name)

greet("Hriday")

👉 Output:

Hello Hriday


---

3. Functions with No Arguments & No Return

Just does a task, no input, no output.

def say_hello():
    print("Hello World")

say_hello()


---

4. Functions with Arguments (Input)

Takes some input and does work.

def square(num):
    print(num * num)

square(5)   # Output: 25


---

5. Functions with Return (Output)

Gives something back after calculation.

def add(a, b):
    return a + b

result = add(10, 20)
print(result)   # Output: 30

👉 Here return is like sending the result back to you.


---

6. Default Argument Function

If you don’t give input, it uses a default value.

def greet(name="Friend"):
    print("Hello", name)

greet()          # Output: Hello Friend
greet("Hriday")  # Output: Hello Hriday


---

7. Keyword Arguments

You can specify arguments by name.

def introduce(name, age):
    print("I am", name, "and I am", age, "years old.")

introduce(age=25, name="Hriday")


---

8. Variable-Length Arguments

When you don’t know how many inputs you’ll get.

🔹 *args (many positional arguments → like a list)

def add_all(*numbers):
    return sum(numbers)

print(add_all(1,2,3,4,5))   # Output: 15

🔹 **kwargs (many keyword arguments → like a dictionary)

def show_info(**details):
    for key, value in details.items():
        print(key, ":", value)

show_info(name="Hriday", role="WFM Analyst", city="Kolkata")


---

9. Lambda Function (Anonymous Function)

A tiny one-line function without def.

square = lambda x: x*x
print(square(6))   # Output: 36

👉 Use it when you need a short throwaway function.


---

🟢 Quick Summary (Like a Menu Card 🍽️)

Built-in functions → Ready-made (e.g., print, len).

User-defined functions → You create with def.

No argument & no return → Just does a task.

With arguments → Needs input.

With return → Gives output.

Default argument → Uses default value if no input.

Keyword arguments → Pass by name.

Variable-length → *args and **kwargs.

Lambda → One-line quick function.



---

👉 In layman’s terms:

Functions = shortcuts.

Instead of writing the same steps 10 times, you make a function once and use it anywhere.



---

Would you like me to also create a real-world WFM example (like a function that calculates SLA or Forecast Accuracy) so it connects directly with your work?


