import numpy as np

A=np.array([[1,2,3],[4,5,6],[7,8,9]])
Z=np.array([1,0,-1])
print("MATRIX VECTOR MULTIPLICATION :\n",np.dot(A,Z))

I=np.eye(3)
print(np.dot(A,I))