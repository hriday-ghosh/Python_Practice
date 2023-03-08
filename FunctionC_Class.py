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
