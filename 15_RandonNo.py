#in numpy Random() is used to generate random no to perform diffrent type operation


#Genrating integer no using random()
import  numpy as np
rand=np.random.randint(10)
print(rand)

#genrating the float no 
rand=np.random.rand(2)
print(rand)

#genrating random array just give the element size in bracket by using size keyword
rand=np.random.randint(100 , size=(2))
print(rand)

# generating 2-D array
rand=np.random.randint(100, size=(2,3))
print(rand)

#Choice()-> to choice the genrate random no from given array

rand=np.random.choice([2,3,4,5,33,45,65])
print(rand)


'''
Q-> make a 4x4 2-D array using only 2,3,4,5

'''
import numpy as np
rando=np.random.choice([2,3,4,5] ,size=(4,4))
print(rando)