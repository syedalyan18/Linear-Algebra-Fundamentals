import sympy as sp

x=sp.Symbol('x')
f=sp.exp(-x)

indef_integral=sp.integrate(f,x)
def_integral=sp.integrate(f,(x,0,sp.oo))

print("INDEFINITE INTEGRAL : ",indef_integral)
print("DEFINITE INTEGRAL : ",def_integral)