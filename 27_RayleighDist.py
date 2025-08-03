#rayleigh distribution is used for get distance of 2 normal vaiables from origin
import numpy as np
ray=np.random.rayleigh(scale=2, size=(2,3))  # Generate samples from a Rayleigh distribution with scale parameter 2
print(ray)  

# Visualizing the Rayleigh distribution
import matplotlib.pyplot as plt
import seaborn as sns
sns.displot(ray, kde=True)  # Plot the distribution with a kernel density estimate
plt.title('Rayleigh Distribution (scale=2)')
plt.xlabel('Value')
plt.ylabel('Density')
plt.show()  # Display the distribution plot of the Rayleigh distribution

    