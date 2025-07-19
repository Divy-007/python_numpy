#basic bololean filtering   
import numpy as np
printt=np.array([33,4,4,5,5,])
filter=printt>5  #firstly filtering condition which give true false
print(filter)
filter_arr=printt[filter] # now choosse that true element 
print(filter_arr)

#filtering shortcut or direct method
filter_arr=printt[printt>4] # direct 
print(filter_arr)


"""
Q-> print only even no using filtering
"""
import numpy as np
arr=np.array([22,34,44,55,23,50,45,3,432,34,24,44,56])
filter_arr=arr[arr%2==0]
print(filter_arr)
