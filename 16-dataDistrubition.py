#probality fun - we can generate random no based on probalties
import numpy as np
rand=np.random.choice([1,3,5,7] , p=[0.1,0.3,0.5,0.1],size=(100))
print (rand)

# for 2-D array
rand=np.random.choice([1,2,3,4,5], p=[0.1,0.2,0.4,0.1,0.2] , size=[2,3])
print(rand)
