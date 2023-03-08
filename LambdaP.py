# from functools import reduce

# l = [1, 2, 3, 4]

# print(reduce(lambda a, b: a*b, l))

# def outer_function(x):
#     def inner_function(y):
#         return x + y
#     return inner_function


# add_5 = outer_function(10)
# print(add_5(7))


# l = [2, 3, 4, 5]
# try:
#     for i in range(len(l)):
#         print(l)
# except:
#     print("Not working")


l = [1, 2, 3, 4]

print((lambda a, b: a*b, l))
