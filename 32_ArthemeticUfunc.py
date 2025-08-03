#Arthemetic ufuncs in numpyare used to perform basic arithmetic operations like addition, subtraction, multiplication, and division.
# Examples: np.add, np.subtract, np.multiply, np.divide
import numpy as np
# Example of using arithmetic ufuncs
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([10, 20, 30, 40, 50])
print(np.add(arr1, arr2))  # Using np.add to add elements of two arrays
print(np.subtract(arr1, arr2))  # Using np.subtract to subtract elements of two
print(np.multiply(arr1, arr2))  # Using np.multiply to multiply elements of two arrays
print(np.divide(arr1, arr2))  # Using np.divide to divide elements of two


# Example of using arithmetic ufuncs with broadcasting
arr3 = np.array([1, 2, 3])
arr4 = np.array([[10], [20], [30]])
print(np.add(arr3, arr4))  # Broadcasting addition of arr3 and arr4
# Example of using arithmetic ufuncs with scalar values
scalar_value = 5
print(np.multiply(arr1, scalar_value))  # Multiplying each element of arr1 by scalar_value
