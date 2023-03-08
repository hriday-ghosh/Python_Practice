from unicodedata import name


def test9():
    L = [2, 3, 4, 5]
    a = 0
    for i in L:
        return (L)


test9()

# Finding out Age:

Name = input("name: ")
POB = input("Birth Place: ")
YOB = int(input("Year_Birth"))

Age = 2022-YOB

print(f"""
What is the name: {Name}

What is the Birth place: {POB}

What is the age: {Age}

"""
      )


# Calculator:

a = int(input("What is the first no= "))
b = int(input("What is the second no. = "))
c = a*b
d = a/b
e = a+b
f = a-b

print(f"{a} Addition {b} is {e}")
print(f"{a} - {b} is {f}")
print(f"{a} * {b} is {c}")
print(f"{a} / {b} is {d}")


#print("The Multiplication is " f"{c}")
#print("The Division is " f"{d}")
#print("The Addition is " f"{e}")
#print("The Subtraction is " f"{f}")


# Calculator 02:

a = int(input("What is the first no= "))
b = int(input("What is the second no. = "))
choice = input('Enter the operation +,-,*')
if choice == '+':
    e = a+b
    print(f"{a} Addition {b} is {e}")

elif choice == '-':
    f = a-b
    print(f"{a} - {b} is {f}")


elif choice == '*':
    c = a*b
    print(f"{a} * {b} is {c}")

else:
    print('wrong operation')


# FString Example:


name = input("Enter your name:")

print(f"You have entered: {name}")


# Date Findout:

date = input("Write like 08/12/2022 ")
today = date[0:2]
month = date[3:5]
year = date[6:]
print(f"{today} is the date and {month} is the month {year} is the year")


# Findding Lenght:
def lenn(s):
    count = 0
    for i in s:
        count = count+1
        return count


lenn("Hriday")

# Finding Opposite
name = "012345789"
print(name[::-1])


# Condition Checking
BIKE = False
CAR = True
TRAVEL_100_KM = BIKE and CAR

print(f"You have BIKE: {BIKE}")
print(f"You have CAR: {CAR}")
print(f"You can travel 100 KMs: {TRAVEL_100_KM}\n")

# # Block Four
# BIKE = False
# CAR = False
# TRAVEL_100_KM = BIKE or CAR

# print(f"You have BIKE: {BIKE}")
# print(f"You have CAR: {CAR}")
# print(f"You can travel 100 KMs: {TRAVEL_100_KM}\n")


# A = [1, 2, 3, 4]
# ans = [itms**2 for itms in A]

# print(ans)

# Inputs = input("Enter Student Name: ")
# Student_Names = [["Ram", 95], ["Shyam", 85]]
# if Inputs == "Ram":
#     print("Ram's no is" [0, 1])
# else:
#     print("Students is no mathed")
# if Inputs == "Shyam":
#     print(f"Shyam no is" [1][2])
# else:
#     print("Students is no mathed")


# Inputs = input("Enter Student Name: ")
# Student_Names = [["Ram", 95], ["Shyam", 85]]
# if Inputs == "Ram":
#     print(f"Ram's no is {Student_Names[0][1]}")
# else:
#     print("Students is no mathed")
# if Inputs == "Shyam":
#     print(f"Shyam no is {Student_Names[1][1]}")
# else:
#     print("Students is no mathed")


# Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.


spam = input("Enter your no or character:- ")

if spam == "1":
    print('Hello')
elif spam == "2":
    print('Howdy')
else:
    print('Greetings!')
