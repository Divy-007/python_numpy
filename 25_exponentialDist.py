#Exponential Distribution
# It is used to model the time b/w event in in a poisson process
import numpy as np
expo=np.random.exponential(scale=2, size=(2,3))  # Generate 1000 samples from an exponential distribution
print(expo)

# Visualizing the exponential distribution
import matplotlib.pyplot as plt
import seaborn as sns
sns.displot(expo, kde=True)  # Plot the distribution with a kernel density estimate
plt.title('Exponential Distribution (scale=2)')
plt.xlabel('Value')             
plt.ylabel('Density')
plt.show()  # Display the distribution plot of the exponential distribution