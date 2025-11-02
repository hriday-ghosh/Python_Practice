# NumPy Basic and Advanced Syntaxes Explained Simply and Clearly with OUTPUT
# --------------------------------------------------------------------------

import numpy as np   # Importing the NumPy library and naming it as 'np'
                     # NumPy helps handle numbers, lists, and matrices efficiently
                     # It is widely used in Data Analysis, AI, and Machine Learning


# ---------------- BASIC ----------------

# 1. Create Arrays
arr1 = np.array([1, 2, 3])          # Creates a 1D array → like a simple list [1, 2, 3]
arr2 = np.array([[1, 2], [3, 4]])   # Creates a 2D array (matrix)
                                    # [
                                    #  [1, 2],
                                    #  [3, 4]
                                    # ]

# 2. Check array properties
print(arr1.shape)   # (3,) → means 1D array with 3 elements
print(arr2.shape)   # (2, 2) → 2 rows, 2 columns
print(arr1.dtype)   # int64 → shows data type (may vary by system)
print(arr2.ndim)    # 2 → number of dimensions (1D or 2D)

# ---------- OUTPUT ----------
# (3,)
# (2, 2)
# int64
# 2


# 3. Create special arrays
zeros = np.zeros((2, 3))   # Creates 2x3 matrix of 0s
ones = np.ones((2, 2))     # Creates 2x2 matrix of 1s
full = np.full((2, 2), 7)  # Creates 2x2 matrix filled with 7
identity = np.eye(3)       # Creates a 3x3 identity matrix (1s on diagonal)
                           # [
                           #  [1. 0. 0.]
                           #  [0. 1. 0.]
                           #  [0. 0. 1.]
                           # ]


# 4. Generate ranges
arr_range = np.arange(0, 10, 2)  # Creates numbers from 0 to 8 (10 excluded), step = 2
# Output → [0 2 4 6 8]

lin_space = np.linspace(0, 1, 5) # Creates 5 evenly spaced numbers between 0 and 1
# Output → [0.   0.25 0.5  0.75 1.  ]


# 5. Reshape arrays
reshaped = np.array([1, 2, 3, 4, 5, 6]).reshape((2, 3))
# Reshape → 2 rows, 3 columns
# [
#  [1 2 3]
#  [4 5 6]
# ]


# 6. Indexing & Slicing
print(arr1[0])       # Prints first item of arr1 → 1
print(arr2[1, 1])    # 2nd row, 2nd column → 4
print(arr2[:, 0])    # ":" = all rows, first column → [1 3]

# ---------- OUTPUT ----------
# 1
# 4
# [1 3]


# 7. Mathematical Operations
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(a + b)          # Adds element-wise → [5 7 9]
print(a * b)          # Multiplies element-wise → [4 10 18]
print(a ** 2)         # Squares each → [1 4 9]
print(np.sqrt(a))     # Square root of each → [1.         1.41421356 1.73205081]

# ---------- OUTPUT ----------
# [5 7 9]
# [ 4 10 18]
# [1 4 9]
# [1.         1.41421356 1.73205081]


# 8. Aggregate Functions
print(np.sum(arr2))   # Adds all numbers → 10
print(np.min(arr2))   # Smallest value → 1
print(np.max(arr2))   # Largest value → 4
print(np.mean(arr2))  # Average → 2.5
print(np.std(arr2))   # Standard deviation → 1.118...

# ---------- OUTPUT ----------
# 10
# 1
# 4
# 2.5
# 1.118033988749895


# 9. Boolean Masking
mask = arr2 > 2       # True where condition met
# mask → [[False False]
#          [ True  True]]
print(arr2[mask])     # Shows elements where True → [3 4]

# ---------- OUTPUT ----------
# [3 4]


# 10. Copy vs View
x = np.array([1, 2, 3])
y = x.copy()          # .copy() makes a real copy
y[0] = 100            # Changes only y, not x
print(x)              # [1 2 3]
print(y)              # [100   2   3]

# ---------- OUTPUT ----------
# [1 2 3]
# [100   2   3]


# 11. Random Numbers
rand_arr = np.random.rand(2, 2)
# Random floats between 0 and 1 (values change every run)
# Example → [[0.42 0.88]
#            [0.15 0.77]]

rand_ints = np.random.randint(1, 10, (2, 3))
# Random integers from 1 to 9 (values change every run)
# Example → [[3 7 5]
#            [8 2 4]]


# 12. Axis (direction of operation)
arr3 = np.array([[1, 2, 3], [4, 5, 6]])
print(np.sum(arr3, axis=0))  # Sum column-wise → [5 7 9]
print(np.sum(arr3, axis=1))  # Sum row-wise → [6 15]

# ---------- OUTPUT ----------
# [5 7 9]
# [6 15]


# ---------------- ADVANCED ----------------

# 13. Broadcasting
m = np.array([[1], [2], [3]])  # (3,1)
n = np.array([10, 20, 30])     # (3,)
result = m + n
print(result)
# NumPy automatically matches shapes and adds them
# Output:
# [[11 21 31]
#  [12 22 32]
#  [13 23 33]]

# ---------- OUTPUT ----------
# [[11 21 31]
#  [12 22 32]
#  [13 23 33]]


# 14. Stacking Arrays
arr_a = np.array([1, 2])
arr_b = np.array([3, 4])
print(np.vstack((arr_a, arr_b)))  # Stack vertically → one below another
print(np.hstack((arr_a, arr_b)))  # Stack horizontally → side by side

# ---------- OUTPUT ----------
# [[1 2]
#  [3 4]]
# [1 2 3 4]


# 15. Splitting Arrays
big_arr = np.array([1, 2, 3, 4, 5, 6])
print(np.split(big_arr, 3))  # Split equally into 3 small arrays

# ---------- OUTPUT ----------
# [array([1, 2]), array([3, 4]), array([5, 6])]


# 16. Advanced Indexing
data = np.array([10, 20, 30, 40])
indices = [0, 2]          # Positions 0 and 2
print(data[indices])      # Picks [10 30]

# ---------- OUTPUT ----------
# [10 30]


# 17. Where Function
arr4 = np.array([5, 15, 25, 35])
labels = np.where(arr4 > 20, 'High', 'Low')
print(labels)
# If element >20 → 'High', else → 'Low'
# ---------- OUTPUT ----------
# ['Low' 'Low' 'High' 'High']


# 18. Unique and Sorting
arr5 = np.array([3, 1, 2, 3, 4, 2])
print(np.unique(arr5))   # Unique values only → [1 2 3 4]
print(np.sort(arr5))     # Sorted order → [1 2 2 3 3 4]

# ---------- OUTPUT ----------
# [1 2 3 4]
# [1 2 2 3 3 4]


# 19. Dot Product (Matrix Multiplication)
m1 = np.array([[1, 2], [3, 4]])
m2 = np.array([[5, 6], [7, 8]])
print(np.dot(m1, m2))
# Multiplication rule → row of first * column of second
# [[(1*5+2*7) (1*6+2*8)]
#  [(3*5+4*7) (3*6+4*8)]]
# [[19 22]
#  [43 50]]

# ---------- OUTPUT ----------
# [[19 22]
#  [43 50]]


# 20. Save and Load Arrays
np.save('my_array.npy', arr1)      # Saves array arr1 into file 'my_array.npy'
loaded_arr = np.load('my_array.npy')  # Loads it back from file
print(loaded_arr)                  # Prints → [1 2 3]

# ---------- OUTPUT ----------
# [1 2 3]




# Now you're ready to work with both basic and advanced NumPy!





Looping in NumPy (with full explanation)

# First, we import NumPy library
import numpy as np

# -----------------------------
# 📌 Example 1: 1D Dataset
# This is like having sales data for 4 days
arr = np.array([10, 20, 30, 40])

# Show the dataset
print("Dataset (1D Array):", arr)   # [10 20 30 40]


# 🔹 1. Simple Loop → go through each number one by one
for x in arr:                 # take each element from the array one by one
    print("Value:", x)        # print that element

➡ Output:

Dataset (1D Array): [10 20 30 40]
Value: 10
Value: 20
Value: 30
Value: 40


---

# 🔹 2. Loop with Index → know both position & value
for i in range(len(arr)):                # range(len(arr)) = [0,1,2,3]
    print("Index:", i, "Value:", arr[i]) # arr[i] gives value at that position

➡ Output:

Index: 0 Value: 10
Index: 1 Value: 20
Index: 2 Value: 30
Index: 3 Value: 40


---

# -----------------------------
# 📌 Example 2: 2D Dataset
# This is like sales data for 2 weeks
# Each row = 1 week, each column = day of week
arr2 = np.array([[1, 2, 3],
                 [4, 5, 6]])

# Show the dataset
print("Dataset (2D Array):\n", arr2)
# [[1 2 3]
#  [4 5 6]]


# 🔹 3. Loop row by row
for row in arr2:               # each row means 1 week
    print("Row (Week):", row)  # prints the whole row

➡ Output:

Dataset (2D Array):
 [[1 2 3]
 [4 5 6]]
Row (Week): [1 2 3]
Row (Week): [4 5 6]


---

# 🔹 4. Nested Loop → go inside each row, number by number
for row in arr2:           # pick one row at a time
    for val in row:        # inside that row, pick each value
        print("Value:", val)

➡ Output:

Value: 1
Value: 2
Value: 3
Value: 4
Value: 5
Value: 6


---

# 🔹 5. Smart Way → np.nditer()
# np.nditer() helps to go through every element easily, no matter 1D or 2D
for x in np.nditer(arr2):
    print("Value:", x)

➡ Output:

Value: 1
Value: 2
Value: 3
Value: 4
Value: 5
Value: 6


---

# 🔹 6. BEST Way → Vectorization 🚀
# Instead of looping, NumPy can apply math to whole array at once
print("Double Values:", arr * 2)
# This means multiply each element of arr by 2 automatically

➡ Output:

Double Values: [20 40 60 80]


---

🎯 Layman Summary

for x in arr → take one number at a time.

for i in range(len(arr)) → take position + number.

for row in arr2 → take one row (like a week).

nested loop → take row, then number inside row.

np.nditer() → shortcut to pick all numbers one by one.

Vectorization → fastest way, do math on full dataset in one shot.

# Import NumPy
import numpy as np

# Create a dataset (1D Array)
# Think of this as sales data for 4 days
arr = np.array([10, 20, 30, 40])

print("Original Dataset:", arr)   # [10 20 30 40]


# 🔹 Without Vectorization (using loop)
# Multiply each element by 2 using loop
new_list = []                         # create an empty list to store results
for x in arr:                         # take each number from arr
    new_list.append(x * 2)            # multiply it by 2 and add to list
print("Using Loop:", new_list)        # [20, 40, 60, 80]


# 🔹 With Vectorization (NumPy way 🚀)
# Directly multiply whole array by 2 at once
new_arr = arr * 2                     # NumPy applies *2 to all elements automatically
print("Using Vectorization:", new_arr) # [20 40 60 80]

Original Dataset: [10 20 30 40]
Using Loop: [20, 40, 60, 80]
Using Vectorization: [20 40 60 80]

# Create a 2D dataset (2 weeks × 3 days sales data)
arr2 = np.array([[1, 2, 3],
                 [4, 5, 6]])

print("Original Dataset:\n", arr2)
# [[1 2 3]
#  [4 5 6]]


# Multiply all values by 10 (like converting sales into rupees)
new_arr2 = arr2 * 10     # Vectorization applies *10 to every element
print("After Vectorization:\n", new_arr2)
# [[10 20 30]
#  [40 50 60]]

Original Dataset:
 [[1 2 3]
 [4 5 6]]
After Vectorization:
 [[10 20 30]
 [40 50 60]]




    import numpy as np   # Importing the numpy library and giving it a short name 'np' 
                     # (so we can use np instead of typing numpy again and again)

# ------------------ ARRAY CREATION ------------------

A = np.array([1,2,3])   
# Creates a 1-dimensional array (like a simple list)
# [1, 2, 3]
# Shape → (3,)  meaning it has 3 elements in one row
# Used when you want to store or do math on a 1D list of numbers

B = np.array([[1,2,3],[4,5,6]])  
# Creates a 2-dimensional array (like rows and columns)
# [
#  [1, 2, 3],
#  [4, 5, 6]
# ]
# Shape → (2, 3) meaning 2 rows and 3 columns
# Used for working with matrices or tables

C = np.array([[[1,2],[3,4]], [[5,6],[7,8]]])  
# Creates a 3-dimensional array (like a cube of numbers)
# Think of it as 2 layers, each layer is a 2x2 matrix
# Shape → (2, 2, 2)
# Used in advanced operations like image data or 3D data

D = np.array([1,2,3], dtype=float)
# Same as array A but with data type set to 'float' (decimal numbers)
# Output → [1.0, 2.0, 3.0]
# dtype means "data type" – you can set it to int, float, complex, etc.

E = np.arange(1,12,2)
# Creates an array from 1 up to (but not including) 12, with a step of 2
# Output → [1, 3, 5, 7, 9, 11]
# arange(start, stop, step) works like Python's range() but gives an array
# Useful for generating number sequences quickly

F = np.arange(16).reshape(2,2,2,2)
# np.arange(16) → makes numbers 0 to 15 (16 numbers)
# reshape(2,2,2,2) → reshapes it into a 4-dimensional array
# So shape → (2, 2, 2, 2)
# Basically 2 blocks → each having 2x2x2 cubes
# Used in multidimensional data or tensor operations

G = np.ones((3,3))
# Creates a 3x3 array filled with 1s
# Shape → (3,3)
# Useful for initializing arrays or matrices with all 1s before operations

H = np.zeros((3,3))
# Creates a 3x3 array filled with 0s
# Shape → (3,3)
# Useful for initializing arrays with all zeros (like placeholders)

I = np.random.random((3,4))
# Creates a 3x4 array filled with random numbers between 0 and 1
# Shape → (3,4)
# Useful in simulations, testing, or machine learning initialization

J = np.linspace(-10,10,10, dtype=int)
# Creates 10 evenly spaced numbers from -10 to 10 (including both ends)
# dtype=int means all numbers will be integers
# Output → [-10, -7, -5, -2, 0, 2, 5, 7, 10, 10]
# linspace(start, stop, num) gives equal intervals between start and stop

K = np.identity(3)
# Creates a 3x3 Identity matrix
# [
#  [1, 0, 0],
#  [0, 1, 0],
#  [0, 0, 1]
# ]
# Identity matrix → 1s on the diagonal and 0s elsewhere
# Very important in matrix algebra (acts like ‘1’ in multiplication)

print(K)  
# Prints the identity matrix on the screen

