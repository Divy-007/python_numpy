"""
used for discrete outcome -yes/no, success/failure 
"""
"""
binaomial distribution is a discrete probability distribution that describes the number of successes in a "fixed number "of independent Bernoulli trials, each with the same probability of success."""

import numpy as np
#Q- genarate a random binomial distribution of 2*3 with 5 trials and prob of success at 0.5
binom = np.random.binomial(n=5, p=0.5, size=(2, 3))
print(binom)            

#VISUALIZING
import matplotlib.pyplot as plt
import seaborn as sns
sns.displot(binom, kde=True)
plt.show()