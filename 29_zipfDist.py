#zipf distribution is work on rank-frequency rule 
#which will be on rank 1  will be more frequent than rank 2 and so on
import numpy as np
zip=np.random.zipf(a=2, size=(2, 3))  # Generate samples from a Zipf distribution with exponent parameter 2
print(zip)  

# Visualizing the Zipf distribution
import matplotlib.pyplot as plt
import seaborn as sns
sns.displot(zip, kde=True)  # Plot the distribution with a kernel density estimate
plt.title('Zipf Distribution (a=2)')
plt.xlabel('Value')
plt.ylabel('Density')
plt.show()  # Display the distribution plot of the Zipf distribution
