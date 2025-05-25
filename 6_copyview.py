#difrence between numpy array copy an d view


# we will make a array and then make copy it and and view ir and after it we will make change and again print copy and view 
import numpy as np
devu=np.array([1,2,3,4,5])
devu1=devu.copy()
devu2=devu.view()
print("printing all array before changing value ")
print(devu,"it is original array ")
print(devu1,"copy array")
print(devu2,"view array")
devu[0]=0
print("calling copy array and view array after make changes in original array")
print(devu,"original array has change")
print(devu1,"copy array will not change untill we make chnage in copy array")
print(devu2,"view array also has been changed as original one")