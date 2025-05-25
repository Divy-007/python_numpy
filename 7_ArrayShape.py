#the shape of an array is the no element in EACH dimension

#here i create a 3-d array and trying to get it shape
#the o/p should be 2,2,3     
#cause the first dimemsion hold 2 elememt and second also 2 and last contain 3 element
import numpy as np 
devu=np.array([[[1,2,3,],[4,5,6,]] ,[[1,2,3],[4,56,6]]])
print(devu.shape)


#here i again created 3-D array but 2nd dimension have difrent element
#this code will be give error becuse to make nd array the array should be in structure

import numpy as np
devu=np.array([[[1,2,3,],[4,5,6,]] ,[[4,56,6]]])
print(devu.shape)