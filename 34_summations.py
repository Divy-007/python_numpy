#we know addition is done between two arrays or arguments 
#but summation is done between all the elements of an array


#summation is done using np.sum() function
#it takes an array as input and returns the sum of all elements in the array
import numpy as np
# Example of summation
arr = np.array([1, 2, 3, 4, 5])
sum_result = np.sum(arr)  # Summing all elements of the array
print("Sum of array elements:", sum_result)  # Output: 15


#summation over an axis 
import numpy as np
# Example of summation over an axis
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
sum_result_axis0 = np.sum(arr_2d, axis=0)  # Summing along rows (columns remain)
sum_result_axis1 = np.sum(arr_2d, axis=1)  # Summing along columns (rows remain)
print("Sum along axis 0 (columns):", sum_result_axis0)  # Output: [5 7 9]
print("Sum along axis 1 (rows):", sum_result_axis1)  # Output
# Output: [ 6 15]

#commulative summation

#it partially sum the elements of an array
#for exxample , arr[1,2,3,4,] = [1,1+2,1+2+3,1+2+3+4] = [1,3,6,10]

arr = np.array([1, 2, 3, 4])
cumsum_result = np.cumsum(arr)  # Cumulative sum of the array
print("Cumulative sum of array elements:", cumsum_result)  # Output: [ 1  3  6 10]
