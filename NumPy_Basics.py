# NumPy Basic and Advanced Syntaxes Explained Simply

import numpy as np  # Import NumPy

# ---------------- BASIC ----------------

# 1. Create Arrays
arr1 = np.array([1, 2, 3])  # 1D array
arr2 = np.array([[1, 2], [3, 4]])  # 2D array

# 2. Check array properties
print(arr1.shape)  # (3,) means 1D with 3 elements
print(arr2.shape)  # (2, 2) means 2x2 matrix
print(arr1.dtype)  # data type like int64
print(arr2.ndim)  # number of dimensions (1 for 1D, 2 for 2D)

# 3. Create special arrays
zeros = np.zeros((2, 3))  # matrix of 0s
ones = np.ones((2, 2))  # matrix of 1s
full = np.full((2, 2), 7)  # matrix filled with 7
identity = np.eye(3)  # identity matrix (1s in diagonal, rest 0)

# 4. Generate ranges
arr_range = np.arange(0, 10, 2)  # numbers from 0 to 8 with step 2
lin_space = np.linspace(0, 1, 5)  # 5 evenly spaced numbers from 0 to 1

# 5. Reshape arrays
reshaped = np.array([1, 2, 3, 4, 5, 6]).reshape((2, 3))  # 2 rows, 3 cols

# 6. Indexing & Slicing
print(arr1[0])  # first item of 1D array
print(arr2[1, 1])  # value at 2nd row, 2nd column
print(arr2[:, 0])  # all rows, first column

# 7. Mathematical Operations
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(a + b)  # element-wise addition
print(a * b)  # element-wise multiplication
print(a ** 2)  # square of each element
print(np.sqrt(a))  # square root of each element

# 8. Aggregate Functions
print(np.sum(arr2))  # sum of all values
print(np.min(arr2))  # smallest number
print(np.max(arr2))  # largest number
print(np.mean(arr2))  # average
print(np.std(arr2))  # standard deviation

# 9. Boolean Masking
mask = arr2 > 2  # condition returns True/False for each element
print(arr2[mask])  # shows values where condition is True

# 10. Copy vs View
x = np.array([1, 2, 3])
y = x.copy()  # makes a real copy of x
y[0] = 100  # changing y won't affect x
print(x)  # original remains unchanged
print(y)  # modified copy

# 11. Random Numbers
rand_arr = np.random.rand(2, 2)  # random float values in 2x2
rand_ints = np.random.randint(1, 10, (2, 3))  # random ints 1 to 9 in 2x3

# 12. Axis
arr3 = np.array([[1, 2, 3], [4, 5, 6]])
print(np.sum(arr3, axis=0))  # sum down each column
print(np.sum(arr3, axis=1))  # sum across each row

# ---------------- ADVANCED ----------------

# 13. Broadcasting
m = np.array([[1], [2], [3]])  # column vector shape (3,1)
n = np.array([10, 20, 30])    # row vector shape (3,)
result = m + n  # shapes broadcast to (3,3)
print(result)  # adds each row to the full row vector

# 14. Stacking Arrays
arr_a = np.array([1, 2])
arr_b = np.array([3, 4])
print(np.vstack((arr_a, arr_b)))  # stack arrays vertically (rows)
print(np.hstack((arr_a, arr_b)))  # stack arrays horizontally (columns)

# 15. Splitting Arrays
big_arr = np.array([1, 2, 3, 4, 5, 6])
print(np.split(big_arr, 3))  # split into 3 equal parts

# 16. Advanced Indexing
data = np.array([10, 20, 30, 40])
indices = [0, 2]  # positions to extract
print(data[indices])  # select items at index 0 and 2

# 17. Where Function
arr4 = np.array([5, 15, 25, 35])
labels = np.where(arr4 > 20, 'High', 'Low')  # condition-based labeling
print(labels)  # outputs array with 'High' or 'Low' strings

# 18. Unique and Sorting
arr5 = np.array([3, 1, 2, 3, 4, 2])
print(np.unique(arr5))  # returns sorted array with unique values
print(np.sort(arr5))  # returns sorted version of array

# 19. Dot Product (Matrix Multiplication)
m1 = np.array([[1, 2], [3, 4]])
m2 = np.array([[5, 6], [7, 8]])
print(np.dot(m1, m2))  # multiply 2 matrices

# 20. Save and Load Arrays
np.save('my_array.npy', arr1)  # saves array to .npy file
loaded_arr = np.load('my_array.npy')  # loads array back
print(loaded_arr)

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