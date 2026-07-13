import numpy as np

A = np.array([[4, 7],
              [2, 6]])

# Compute determinant
det = np.linalg.det(A)
print("Determinant:", det)

# Compute inverse
if det != 0: 
    inv = np.linalg.inv(A)
    print("Inverse:\n", inv)
else:
    print("Matrix is singular, inverse does not exist.")
