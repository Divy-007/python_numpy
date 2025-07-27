"""
"In numpy you can genrate random no that follows normal distribution(gaussian distribution)"
"""
"""
loc- mean
scale - SD
size- no of random value u want
"""

#Q- genarate a random normal distribution of 2*3 with mean at 1 and SD of 2

import numpy as np
norm=np.random.normal(loc=1,scale=2,size=(2,3))
print(norm)


#VISUALIZING 

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
scores = random.normal(loc=50, scale=10, size=1000)
sns.displot(scores, kde=True)
plt.show()