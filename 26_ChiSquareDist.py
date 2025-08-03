#chi square distribution
# It is used in hypothesis testing and confidence interval estimation for variance
import numpy as np
chi=np.random.chisquare(df=2, size=(2,3))  # Generate samples from a chi-square distribution with 2 degrees of freedom
print(chi)

# Visualizing the chi-square distribution
import matplotlib.pyplot as plt
import seaborn as sns
sns.displot(chi, kde=True)  # Plot the distribution with a kernel density estimate
plt.title('Chi-Square Distribution (df=2)')
plt.xlabel('Value')
plt.ylabel('Density')
plt.show()  # Display the distribution plot of the chi-square distribution
# It is used to model the distribution of a sum of squared standard normal variables

