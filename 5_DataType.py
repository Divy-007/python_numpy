#there are multiple data type in python 
#i for integer
#f for float
#c for complex float
#s for string
# u for unsigned integer
# o for object
#m for time date
# M for timeDate
#v for memory
#b for boolean

# checking the data type of numpy array  --- >  using'dtype' keyword
import numpy as np 
devu =np.array(["f","f","ndjnfj","hii","hello"])
print(devu.dtype)
#creating array with defined data type 
import numpy as np 
devu =np.array([1,2,3,4,5] , dtype='f')
print(devu)
print(devu.dtype)


#typecasting 


   # Ex-1-  (int to float)  
import numpy as n
devu=np.array([1,2,3,4,5])
devu1=devu.astype('float32')  # to save memory
print(devu1)
print(devu1.dtype)
 
 #Ex-2 (int to bool)
import numpy as np 
devu=np.array([1,0,3,0,4])
devu1=devu.astype('bool')
print(devu1)
print(devu1.dtype)





