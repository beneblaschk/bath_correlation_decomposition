from sympy import * 
#symbols, sin, lambdify, limit
import sympy as sp
from math import * 

# this is the bose 1 branch, where i want to checkout whether 
# the old implementation of the bose functio produced the same results 
# than the updated one, 
# i have some problems syncronizing


x, y, z = symbols('x y z')

# Implementation from: Communication: Padé spectrum decomposition of Fermi function and Bose function

# reference function: 

f_ref = 1/ (1-sp.exp(-x)) 

coeff_list = [0.08333333333333333, -0.0013888888888888874, 3.3068783068782915e-05, -8.267195767195603e-07, 2.0876756987866386e-08, -5.284190138685735e-10, 1.3382536530666791e-11, -3.3896802963044296e-13, 8.586062056093802e-15, -2.1748686983715528e-16, 5.509002826470406e-18, 0, 0, 0, 0]


def coeff(k) :
     return 1


def bose(N, index): 
    if(index==0):
          return 1/x + bose(N-1, index+1)
    if(index==1):
          return 1/2 + bose(N-1, index+1) 
    
    # implement: x \sum_{k=0}^{2N-1}
    aux = x * (coeff_list[index-2] * x**(2*(index-2)))
    print(aux)
    if(N-1==index-2):
         return aux
    else:
         return aux + bose(N, index+1)


print(bose(10,0))

