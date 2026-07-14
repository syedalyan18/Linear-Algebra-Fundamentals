import sympy as sp

x=sp.Symbol('x')
f=x**2

indef_integral=sp.integrate(f,x)
def_integral=sp.integrate(f,(x,0,2))

print("INDEFINITE INTEGRAL : ",indef_integral)
print("DEFINITE INTEGRAL : ",def_integral)
