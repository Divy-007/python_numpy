#in numpy rouinding is used to round the value to nearest integer
#we can round the value to nearest integer, floor value, ceil value,truncate value
#by using np.round, np.floor, np.ceil, np.trunc or np.fix
import numpy as np

#1. truncate value or fix value
arr = np.array([1.5, 2.5, 3.5, 4.5])
print("Truncate value:", np.trunc(arr))  # it just cut the decimal part
print("Fix value:", np.fix(arr))  # same as truncating 


#2. rounding function(around() or round())
arr = np.array([1.5, 2.5, 3.5, 4.5])
print("Rounding value:", np.round(arr))  # rounds to nearest integer

#note- if the decimal part is 0.5, it rounds to the nearest even number
#for example, 2.5 rounds to 2 and 3.5 rounds to 4
#this is known as "round half to even" or "bankers' rounding"

#3. floor function- give the lower integer value
arr = np.array([1.5, 2.5, 3.5, 4.5])
print("Floor value:", np.floor(arr))  # 

#4. ceil function- give the upper integer value(opposite of floor)
arr = np.array([1.5, 2.5, 3.5, 4.5])
print("Ceil value:", np.ceil(arr))  # rounds up to the nearest integer



#note-all function above return float values
#to convert the result to integer, we can use astype(int)