""" from sympy import *

x, y, z = symbols('x y z')

z_0 = symbols('z_0')

f = 1/(x*(x+1)) 
z_0 = 0

print(limit(sin(x)/x,x,0)) """
import sympy as sy

x, y = sy.symbols('x y')

f = x**2

print(f)
y=2
print(f.subs(x,y))

print(sy.sin(sy.pi/2))

print(sy.sin(x))

