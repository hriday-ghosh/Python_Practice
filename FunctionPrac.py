"""
3. Accept an integer as input and print its square as output.

n = int(input("Enter a number: "))
S = n**2
print(S)


By a Function: 
    
    Write a function which can take input and return as function

def sqaure_do():
    X = int(input("Enter a number: "))
    return X*X


resulted = sqaure_do()
print(resulted)


# 4.Accept two integers as input and print their sum as output.


def ADD():
    A = int(input("Enter a number: "))
    B = int(input("Enter a number: "))
    return A+B


Add_Value = ADD()
print(Add_Value)


# 5. Accept two words as input and print the two words after adding a

# space between them

def Add_Word():
    A = str(input("Enter a no. "))
    B = str(input("Enter a no. "))

    return A + " " + B


Word = Add_Word()
print(Word)


# Lamba Function


# join_words = lambda x, y: x + " " + y

# first_word = input("Enter the first word: ")
# second_word = input("Enter the second word: ")

# result = join_words(first_word, second_word)
# print("Result:", result)


"""


# 5. Accept two words as input and print the two words after adding a space between them

def word_joiner(x, y): return x + y


A = str(input("Enter a word : "))
B = str(input("Enter a word : "))
Result = word_joiner(A, B)
print("Result is", Result)
