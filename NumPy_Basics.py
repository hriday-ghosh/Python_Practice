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
