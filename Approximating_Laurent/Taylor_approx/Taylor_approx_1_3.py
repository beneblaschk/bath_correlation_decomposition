from sympy import symbols, sin, lambdify
import sympy as sp
from math import * 
# now i with signularities: 1/x as the first, careful with the devolpment point -> cannot be the singularity 


# Define the symbolic variable
x = symbols('x')
a = symbols('a')

# Define the symbolic function

# Bose function 
f = 1/1-sp.exp(-x)



def taylor(f, a, y, terms, index) : 
    if terms==0:
        print("final: ")
        return f.subs(x,a)/factorial(index)*((y-a)**(index))
    aux = f.subs(x,a)/factorial(index)*((y-a)**(index)) 
    print(float(abs(aux)))
    return aux + taylor(f.diff(x),a,y, terms-1, index+1)



print(float(taylor(f,1,20,60,0)))


