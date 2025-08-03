#we can craeyte our own ufunc using numpy
#we can use np.frompyfunc to create our own ufunc
import numpy as np
def my_add(x, y):
    return x + y
# Create a ufunc from the custom function
my_add_ufunc = np.frompyfunc(my_add, 2, 1)  # 2 inputs, 1 output
# Test the ufunc
arr1 = np.array([1, 2, 3])
arr2 = np.array([10, 20, 30])
result = my_add_ufunc(arr1, arr2)  # Apply the ufunc to the arrays
print(result)  # Output: [11 22 33]

