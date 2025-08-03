#it is probality of Poisson distribution
#who count the event happening in a fixed interval of time or space
#it is used to model the number of events in a fixed interval of time or space
import numpy as np
import matplotlib.pyplot as plt 
devu=np.random.poisson(lam=2,size=10) 
print(devu)
#lam is the average number of events in the interval



#visualizing the poisson distribution
import seaborn as sns
sns.displot(devu, kde=True)
plt.title('Poisson Distribution (λ=2)')
plt.xlabel('Number of Events')
plt.ylabel('Frequency')
plt.show()#it will print the first element of every row in 4-d array
