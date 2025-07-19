#Permutation - Ararngement of item where order matter
#by two method- permutation() and suffle()

#1->shuffle - change in original array
import numpy as np
arr=np.array([23,22,33,11,23,2,3,])
suffle=np.random.shuffle(arr)
print(suffle)
print(arr)


#2-> Permutation -does not change the original array
arr=np.array([23,22,33,11,23,2,3,])
Perm =np.random.permutation(arr)
print(arr)
print(Perm)