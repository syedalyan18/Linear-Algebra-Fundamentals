import numpy as np

A=np.array([[1,2],[3,4]])

eigenvalues,eigenVectors=np.linalg.eig(A)
print("EigenValues : \n",eigenvalues)
print("EigenVectors : \n",eigenVectors)

U,S,Vt=np.linalg.svd(A)
print("U : \n",U)
print("S : \n",S)
print("Vt : \n",Vt)

Sigma=np.zeros((2, 2))
np.fill_diagonal(Sigma,S)
reconstructed= U @ Sigma @ Vt
print("RECONSTRUCTED : \n",reconstructed)