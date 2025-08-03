#it is generalization of binomial distribution but multional can have more than two outcomes
#it is used to model the probability of a random variable that has more than two outcomes
import numpy as np
import matplotlib.pyplot as plt
# Generate a multinomial distribution with 10 trials and probabilities for 3 outcomes
n = 10  # number of trials
p = [0.2, 0.5, 0.3]  # probabilities for each outcome
devu = np.random.multinomial(n, p, size=1)                  
print(devu)


# Visualizing the multinomial distribution
import seaborn as sns
sns.barplot(x=['Outcome 1', 'Outcome 2', 'Outcome 3'], y=devu[0])
plt.title('Multinomial Distribution (n=10, p=[0.2, 0.5, 0.3])')
plt.xlabel('Outcomes')
plt.ylabel('Frequency')
plt.show()  # Display the bar plot of the multinomial distribution
