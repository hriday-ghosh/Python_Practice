"""
What is File loction?

Ans -> File is nothing but name of memory location on the disk that stores data permanently. 

Variables: 
a = 10 

In variables a will store the data when this particular program will once run but if we create a File than no matter what the file will remain active on the disk. 

Syntax: 

FileObj = open("Filepath", "mode")

Open is a function to work with files and work with 2 parameters.



File mode: 

r = read
w = write 
a = append 
rt = Both read and write 
b = binary mode 


File Operations: 

1. create 
2. read 
3. write 
4. delete 
5. copy
6. close

"""

# 1. File creation means opening:
# 1. Syntax
# Var_name = open("File path where need to be created and always use \\", "mode > x means empty file will be created")

# f = open("C:\\Python\\Python\\File\\A.txt", "x")
# print("File has been created")

# 2. File writing -> adding something to the file:

"""
f = open("C:\\Python\\Python\\File\\A.csv", "w")
f.write("This file is created for Hriday\n Hriday")
print("File has been created")
"""

"""

# 3. File Reading:
f = open("C:\\Python\\Python\\File\\A.txt", "r")
# 30 means 30 bites here
print(f.read(30))


4. File Reading using readline:
If we use readline function, then we do not put bite limit

f = open("C:\\Python\\Python\\File\\A.txt", "r")

# readline can read 1 line data only
print(f.readline())


f = open("C:\\Python\\Python\\File\\A.txt", "r")

# readlines can read multiple data and return in a list.
print(f.readlines())


File closing and Error Handling:
File always be closed after read, write

try:
    f = open("C:\\Python\\Python\\File\\A.txt", "r")
    print(f.readlines())
except:
    print("File is not available, create first")
else:

    # Closing always should written in the else block
    f.close()
    print("File is closed now")


# File Copy:
try:
    # First we will provide path and use alias f2
    with open("C:\\Python\\Python\\File\\A.txt") as f2:

        # then we want to write file to w, and whatever written in A folder, need to copy in B Folder
        with open("C:\\Python\\Python\\File\\B.txt", "w") as f3:

            # Then we will take f2's content on var folder,
            for var in f2:

                # Then we will write this content into f3
                f3.write(var)
except:
    print("File is not available, plz create first")
else:
    f2.close()
    print("File is closed now")


File Deletion:

For File deletion we need to import os as file is stored in disk.
then we will use if condition if the file is exists on the spacific path then it will be removed.
Then normal print.

import os
if os.path.exists("C:\\Python\Python\\File\\A.txt"):
    os.remove("C:\\Python\Python\\File\\A.txt")
else:
    print("File not available")

print("File deleted success")

"""

# Example 02

import sys
num1 = int(input("Enter the first no. "))
num2 = int(input("Enter the second num "))
try:
    div = num1/num
    print("Division is ", div)
except:
    print(sys.exc_info()[0])  # It will print exception name
    print(sys.exc_info()[1])  # It will print exception information
print("Rest of the code")
