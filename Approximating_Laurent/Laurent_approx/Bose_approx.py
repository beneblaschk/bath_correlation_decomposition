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

def coeff(k) :
     return 1


def bose(N, index): 
    if(index==0):
          return 1/x + bose(N-1, index+1)
    if(index==1):
          return 1/2 + bose(N-1, index+1) 
    
    # implement: x \sum_{k=0}^{2N-1}
    aux = x * (coeff(index-2) * x**(2*(index-2)))
    print(aux)
    if(N-1==index-2):
         return aux
    else:
         return aux + bose(N, index+1)


print(bose(5,0))

