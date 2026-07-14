import numpy as np
import matplotlib.pyplot as plt

# mu,sigma=0,1
# x=np.linspace(-4,4,100)
# y=(1/np.sqrt(2*np.pi*sigma**2)) *np.exp(-0.5*(x-mu)**2/sigma**2)

# plt.plot(x,y)
# plt.title("Gaussian Distribbution")
# plt.show()

p=0.6
plt.bar([0,1],[1-p,p],color="blue")
plt.title("Bernoulli Distribbution")
plt.xticks([0,1],labels=["0 (failure)","1 (Success)"])
plt.show()
