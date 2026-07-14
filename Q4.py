import sympy as sp

# x=sp.Symbol('x')
# f=x**2
# derivative=sp.diff(f,x)
# print("DERIVATIVE : \n",derivative)

x,y =sp.symbols('x y')
f= 3*x**2 + 5*y**2 + 2*x
grad_x=sp.diff(f,x)
grad_y=sp.diff(f,y)

print("GRADIENTS :")
print("Grad_x : ",grad_x,"\nGrad_y :",grad_y)
