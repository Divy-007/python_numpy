#logistic distribution is similar to the normal distribution but has heavier tails(means it has more probability in the tails(max))
#it is used to model the probability of a random variable that has a finite number of outcomes


#Q-draw 2*2 with mean 1 and sd=2
import numpy as np
import matplotlib.pyplot as plt 
devu = np.random.logistic(loc=1.0, scale=2.0, size=10)
print(devu)


#visualizing the logistic distribution
import seaborn as sns
sns.displot(devu, kde=True)
plt.title('Logistic Distribution (loc=1, scale=2)')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()#it will print the first element of every row in 4-d array
