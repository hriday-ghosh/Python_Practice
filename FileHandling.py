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


# ==========================================
# 🧠 PYTHON FILE HANDLING (EASY NOTES)
# ==========================================
# File handling means - creating, reading, writing, or deleting files.

# ------------------------------------------
# ✳️ OPENING A FILE
# open("filename", "mode")
# mode means what you want to do:
# "r" → read, "w" → write, "a" → append, "x" → create new, "t" → text, "b" → binary

# Example: open file in read mode
file = open("demo.txt", "r")   # open file for reading
print(file.read())             # show all content
file.close()                   # always close file after work


# ------------------------------------------
# ✳️ WRITING TO A FILE
# If file doesn’t exist, it creates a new one.
# If exists, it removes old data and writes new data.

file = open("demo.txt", "w")   # open file to write
file.write("Hello World!\n")   # write text inside file
file.write("I am learning Python.\n")
file.close()                   # close file

# Now check your folder → demo.txt will be created!


# ------------------------------------------
# ✳️ APPENDING TO A FILE (ADD WITHOUT DELETING)
# Append = add more data at the end

file = open("demo.txt", "a")
file.write("Adding one more line.\n")
file.close()


# ------------------------------------------
# ✳️ READING LINE BY LINE

file = open("demo.txt", "r")

# read one line
print("First line:", file.readline())

# read all lines as list
print("All lines:", file.readlines())

file.close()


# ------------------------------------------
# ✳️ USING “with” (No need to close manually)
# "with" automatically closes file after use

with open("demo.txt", "r") as f:
    print("Using WITH block:")
    print(f.read())


# ------------------------------------------
# ✳️ CHECK IF FILE EXISTS

import os

if os.path.exists("demo.txt"):
    print("demo.txt file exists.")
else:
    print("File not found!")


# ------------------------------------------
# ✳️ DELETE A FILE

if os.path.exists("old.txt"):
    os.remove("old.txt")
    print("File deleted!")
else:
    print("old.txt not found, so not deleted.")


# ------------------------------------------
# ✳️ CREATE NEW FILE ONLY IF NOT EXISTS
# "x" → create new file, gives error if already exists

try:
    open("newfile.txt", "x")
    print("newfile.txt created successfully.")
except:
    print("newfile.txt already exists.")


# ------------------------------------------
# ✳️ WORKING WITH BINARY FILES (like image, pdf)
# Binary means non-text data.

# Example: Copy an image
with open("image.jpg", "rb") as old:   # rb = read binary
    with open("copy_image.jpg", "wb") as new:  # wb = write binary
        new.write(old.read())

print("Image copied successfully!")


# ------------------------------------------
# 📝 QUICK RECAP
# open("file.txt", "r") → Read
# open("file.txt", "w") → Write (overwrites)
# open("file.txt", "a") → Append (adds more)
# open("file.txt", "x") → Create new file
# Always close file or use “with”.
# os.remove() → Delete file
# os.path.exists() → Check file exists
