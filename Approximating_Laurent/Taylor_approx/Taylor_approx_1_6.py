from sympy import symbols, sin, lambdify, integrate
import sympy as sp
from math import * 
# trying to integrate the taylor polynom afterwards 


# Define the symbolic variable
x = symbols('x')
a = symbols('a')

# Define the symbolic function

# Bose function 
f = f = 1/(sp.exp(x))
n= 5
a= 1

def taylor(f, a, terms, index) : 
    if terms==0:
        return f.subs(x,a)/factorial(index)*((x-a)**(index))
    aux = f.subs(x,a)/factorial(index)*((x-a)**(index)) 
    #print(aux)
    return aux + taylor(f.diff(x),a,terms-1, index+1)

def print_config(f,taylor_polynom, start, interval, times) : 
    print("configuration: ")
    print(f"function f(x)={f}, taylor polynom : n= {n} developing point = {a}")
    for i in range(0,times): 
        print(f"step: f({start+i*interval:.2f})") 
        step = start+i*interval
        taylor = taylor_polynom.subs(x, step)
        compare = f.subs(x, step) 
        diff = taylor-compare
        print(f"taylor : {float(taylor):.4f} compare: {float(compare):.4f} diff: {float(diff):.4f}")

taylor_polynom = (taylor(f,a,n,0))


#print_config(f,taylor_polynom, 0,1,10) 
print(taylor_polynom)
int_origin = integrate(f, (x, 0, 5))
int_taylor = integrate(taylor_polynom, (x, 0, 15))
print(int_taylor)
print(int_origin)
print(float(int_origin-int_taylor))