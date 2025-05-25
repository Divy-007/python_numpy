#reshaping means changing the shape of an array ,like adding or removiong the element 

#reshaping from 1-D TO 2-D
#note - we can not make change in original array in numpy 
print("rehaping 1-d to 2-d")

import numpy as np
devu=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
devu1=devu.reshape(4,3) #o/p should be [[1,2,3] , [4,5,6] , [7,8,9] , [10,11,12]]
print(devu1)
print("rehaping 1-d to 3-d")
#reshaping from 1-d to 3-D

import numpy as np
devu=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
devu1=devu.reshape(3,2,2) #o/p should be [[[1,2],[3,4]] ,[[5,6],[7,8]] ,[[9,10],[11,12]]]
print(devu1)