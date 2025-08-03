#make for only probality 
#in uniform distribution all outcomes are equally likely
#it is used to model the probability of a random variable that has a finite number of outcomes
import numpy as np
unif=np.random.uniform(low=0.0, high=1.0, size=10)
print(unif)

#visuliztion of uniform distribution
import matplotlib.pyplot as plt
import seaborn as sns
sns.displot(unif, kde=True)
plt.title('Uniform Distribution')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()
#it will print the first element of every row in 4-d array
