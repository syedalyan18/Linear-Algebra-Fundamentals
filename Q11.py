import numpy as np
import matplotlib.pyplot as plt

from scipy.stats import binom,norm,poisson

# Gaussian Distribution
# x=np.linspace(-4,4,100)
# y=norm.pdf(x,loc=0,scale=1)
# plt.plot(x,y,label="Gaussian")
# plt.title("Gaussian Distribution")
# plt.show()

# Binomial Distribution
n,p=10,0.5
x=np.arange(0,n+1)
y=binom.pmf(x,n,p)
plt.bar(x,y, color="green",label="Binomial")
plt.title("Binomial Distribution")
plt.show()

# Poisson Distribution
from scipy.stats import poisson
lam=3
x=np.arange(0,10)
y=poisson.pmf(x,lam)
plt.bar(x,y,color="pink")
plt.title("Poisson Distribution")
plt.show()