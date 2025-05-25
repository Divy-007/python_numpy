#taking an 2-D array [1,2,3,4,5] [6,7,8,9,10] and printing [2,7]
import numpy as np
devu=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(devu[0:2,1])
#now print index 1-4 fro both rows
print(devu[0:2,1:4])
#now work on 3-d and 4-d array
#lets suppose ae have an 3-d array
#it will print 1,2  5,6   9,10  13,14
import numpy as np
devu =np.array([[[1,2,3,4,],[5,6,7,8]] , [[9,10,11,12],[13,14,15,16]]])
print(type(devu))
print(devu[0:2,0:2,0:2])

#now do for 4-d array 
#print first element of every row
print("printing 4-d arrayb element ")
import numpy as np 
devu = np.array([
    [
        [[1,2,3],[4,5,6]],
        [[7,8,9],[10,11,12]]
    ],
    [
        [[13,14,15],[16,17,18]],
        [[19,20,21],[22,23,24]]
    ]
])


print(devu[0:2,0:2,0:2,0])