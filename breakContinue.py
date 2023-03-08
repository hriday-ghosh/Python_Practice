"""
if "a" in "Amazon":
     pass 
    
    # Pass means we will write the next part next time and as we use Pass next condition does not required, code wont show any error
    
    # print("a")

for num in range(1, 11):
    if num % 2 == 0:
        print(num)
        
        So,  here output are 
        
2
4
6
8
10

for num in range(1, 11):
    if num % 2 == 0:
        print(num)
       
       Here output is 
2                                                                         4
6
8
10

Continue:

Now if we use Continue word

for num in range(1, 11):
    if num % 2 == 0:
        continue
    else:
        print(num)

So, here if num % 2 == 0: condition would be skipped due to Continue word so all even no. will not be printed and Odd no. will be printed.

Output is 
1
3
5
7
9


Break: 

When we use break then, it will be out from the loop if the condition once true, and never enter in the loop again

for num in range(1, 11):
    if num % 2 == 0:
        break
    else:
        print(num)
        
        So, here out put is 1
        
"""

# for num in range(1, 11):
#     if num % 2 == 0:
#         # print(num)
#         break
#     else:
#         print(num)


# for i in range(1, 10, 2):
#     print(i)


# for i in range(1, 11):
#     print(i)

# # #0,1,2,3,4,5,6,7,8,9,10
# #  0,1,2,3,4,5,6,7,8,9,10

# i = 0
# while i:
#     i = i+1
#     print(i)
