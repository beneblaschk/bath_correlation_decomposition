from sympy import symbols, sin, lambdify
import sympy as sp
from math import * 
# now i don't want to evalute the function right away, but keep it and then eval it in one go 
# stable running taylor approx


# Define the symbolic variable
x = symbols('x')
a = symbols('a')

# Define the symbolic function

# Bose function 
#f = x/(1+x**2)*(1-sp.exp(x))
f = (x+3) /(1+(x+3)**2)*(1-sp.exp(x+3))
n= 10
a= 1

# now i have the problem that i have a and x to substitute 
# however, there is actually no need for a second a1 

# now i need to subsitute x with a actually 


# Changelog to 1_3 
# CHANGED: removed the parameter for y, because i dont want to eval it at x already 
# CHANGED: print is now only aux, because it is a function and not a value 


def taylor(f, a, terms, index) : 
    if terms==0:
        return f.subs(x,a)/factorial(index)*((x-a)**(index))
    aux = f.subs(x,a)/factorial(index)*((x-a)**(index)) 
    #print(aux)
    return aux + taylor(f.diff(x),a,terms-1, index+1)

#a=1, n=5, f=x**5
#1**5/1 *(x-1)^0 = 1
# + 5*(1**4) * (x-1) = 5*x-5
# + 20*(1**3)/2 (x-1)^2 = 10 * (x-1)^2


h= (taylor(f,a,n,0))
#print(h)


print("configuration: ")
print(f"function f(x)={f}, taylor polynom : n= {n} developing point = {a}")
start = -3
interval = 1
for i in range(0,8): 
    print(f"step: f({start+i*interval:.2f})") 
    step = start+i*interval
    taylor = (h.subs(x, step))
    compare = f.subs(x, step) 
    diff = taylor-compare
    print(f"taylor : {float(taylor):.4f} compare: {float(compare):.4f} diff: {float(diff):.4f}")




