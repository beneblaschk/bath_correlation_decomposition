from sympy import * 
#symbols, sin, lambdify, limit
import sympy as sp
from math import * 
# this is now bath approximation: 



x, y, z = symbols('x y z')



f_ref = 1/ (1-sp.exp(-x)) 

a_0=1/12 

coeff_list = [0.08333333333333333, -0.0013888888888888874, 3.3068783068782915e-05, -8.267195767195603e-07, 2.0876756987866386e-08, -5.284190138685735e-10, 1.3382536530666791e-11, -3.3896802963044296e-13, 8.586062056093802e-15, -2.1748686983715528e-16, 5.509002826470406e-18, 0, 0, 0, 0]
#coeff_list = [0]*15


def sum(k,verbose):
     return sum_recursion(k,0,1,verbose)

def sum_recursion(n, k, gamma,verbose): 
     if (n==k):
          return 0
     
     # (-1)^{k+1} a_k \gamma^{2k+1} 
     aux = (-1)**(k+1) * coeff_list[k]*(gamma)**(2*k+1)
     # aux = coeff_list[k]
     if(verbose):
          print(f"   sum n:{n} k:{k}= {aux}")
     return aux + sum_recursion(n,k+1,gamma,verbose)
s = sum_recursion(11,0,(3),true)
print(s) 


bath = s * sp.exp(x)

print(bath)