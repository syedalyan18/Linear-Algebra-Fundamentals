import numpy as np
import matplotlib.pyplot as plt

from scipy.stats import binom

# n,p=10,0.5
# x=np.arange(0,n+1)
# y=binom.pmf(x,n,p)
# plt.bar(x,y, color="green")
# plt.title("Binomial Distribution")
# plt.show()

from scipy.stats import poisson
lam=3
x=np.arange(0,10)
y=poisson.pmf(x,lam)
plt.bar(x,y,color="pink")
plt.title("Poisson Distribution")
plt.show()