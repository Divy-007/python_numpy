#ufunc in numpy are fast function compared to normal python function
#these are used to perform element wise operation on array
#ufunc are vectorized function
#vectorized function are those which can operate on array without using for loop

"""
#ufunc can be used to perform mathematical operations on arrays
why use u func?-------------------

speed: Ufuncs are implemented in C and optimized for performance, making them faster than equivalent Python loops.
vectorization: Ufuncs operate on entire arrays at once, eliminating the need for explicit loops
# broadcasting: Ufuncs can automatically handle arrays of different shapes and sizes, making them flexible for various operations.
extra powerful features: Ufuncs support additional features like type casting, reducing dimensions, and more, which can simplify complex operations.
"""



"""
categories of ufuncs----------------------------

1. arthemetic ufuncs: These perform basic arithmetic operations like addition, subtraction, multiplication, and division.
   Examples: np.add, np.subtract, np.multiply, np.divide
2. trigonometric ufuncs: These perform trigonometric operations like sine, cosine, and tangent.
   Examples: np.sin, np.cos, np.tan
3. exponential and logarithmic ufuncs: These perform exponential and logarithmic operations.
   Examples: np.exp, np.log, np.log10
4.rounding ufuncs: These perform rounding operations like rounding to the nearest integer, ceiling, and floor.
   Examples: np.round, np.ceil, np.floor
5. comparison ufuncs: These perform element-wise comparisons between arrays.
   Examples: np.equal, np.not_equal, np.greater, np.less
6.stastical ufuncs: These perform statistical operations like mean, median, and standard deviation.
   Examples: np.mean, np.median, np.std
"""

"""
special ufuncs----------------------------

1.reduce: This ufunc reduces an array to a single value by applying a binary operation cumulatively.
   Example: np.add.reduce(arr) sums all elements of the array.

2.accumulate: This ufunc accumulates results of a binary operation across an array, returning an array of the same shape.
   Example: np.add.accumulate(arr) returns a cumulative sum of the array elements.

3.outer: This ufunc computes the outer product of two arrays, resulting in a matrix.
   Example: np.multiply.outer(arr1, arr2) computes the outer product of two arrays
"""




#example of normal python function
import numpy as np
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([10, 20, 30, 40, 50])
arr3=[]
for i,j in zip(arr1, arr2):
    arr3.append(i+j)  # Using a for loop to add elements of two arrays
print(arr3)

#example of ufunc
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([10, 20, 30, 40, 50])
arr3 = np.add(arr1, arr2)  # Using ufunc to add elements of two arrays
print(arr3)  # Output: [11 22 33 44 55]


