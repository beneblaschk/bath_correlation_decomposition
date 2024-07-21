from sympy import symbols, sin, lambdify
from math import factorial
# now i want to extend, so that it is an recursive call
# one could also think when its zero, but this only works if it is a clean polynomial, so i guess no


# Define the symbolic variable
x = symbols('x')
a = symbols('a')

# Define the symbolic function
f = x **2 



def taylor(f, a, y, terms, index) : 
    if terms==0:
        return f.subs(x,a)/factorial(index)*((y-a)**(index))
    return f.subs(x,a)/factorial(index)*((y-a)**(index)) + taylor(f.diff(x),a,y, terms-1, index+1)



print(taylor(f,1,3,4,0))

