"""
items = list()
for item in range(3):
    user_input = input("What would you like to buy? ")
    items = items + [user_input]
    print(items)

Lets make the list for the unlimited user 

items = list()
N = int(input("No of item, would you like to buy: "))
for item in range(3):
    user_input = input("What would you like to buy? ")
    items = items + [user_input]
    print(items)

Lets do it by  While Loop:


items = list()
N = int(input("No of item, would you like to buy: "))
i = 0
while i < N:
    user_input = input("What would you like to buy? ")
    items = items + [user_input]
    i = i + 1
    print(items)

In Method:

If any charachter exists in the list it shows True

A = ["Pen", "Color", "Pencil"]

print("Pen" in A)

NOT IN:

If any charachter exists in the list it shows False

A = ["Pen", "Color", "Pencil"]

print("Pen" not in A)


A = ["Pen", "Color", "Pencil"]

print("Pen" not in A)


"""

# string_example = ["Kol", "JPG", "BLRN", "APDJN"]
# max_len = 0
# result = ''
# for city in string_example:
#     print((string_example(len(city))))
# if len(city) > max_len:
#     result = city

#     print(f"Result: max_len {max_len} name:{result}")


string_example = ["Kol", "JPG", "BLRN", "APDJN"]
max_len = 0
result = ""
l = []
for city in string_example:
    print(
        f"List no {string_example.index} Letter{city} has {len(city)} Alphabates")
