#pareto distribution work on the principle of 80/20 rule
# It is used to model the distribution of wealth, income, or other resources
import numpy as np
pareto = np.random.pareto(a=2, size=(2, 3))  # Generate samples from a Pareto distribution with shape parameter 2
print(pareto)


# Visualizing the Pareto distribution
import matplotlib.pyplot as plt
import seaborn as sns
sns.displot(pareto, kde=True)  # Plot the distribution with a kernel density estimate
plt.title('Pareto Distribution (a=2)')
plt.xlabel('Value')
plt.ylabel('Density')   
plt.show()  # Display the distribution plot of the Pareto distribution