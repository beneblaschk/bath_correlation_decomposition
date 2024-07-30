import scipy.integrate as integrate
import scipy as sc
import numpy
import sympy

import Bose_approx
x, y = sympy.symbols('x y')



coeff_list = [0.08333333333333333, -0.0013888888888888874, 3.3068783068782915e-05, -8.267195767195603e-07, 2.0876756987866386e-08, -5.284190138685735e-10, 1.3382536530666791e-11, -3.3896802963044296e-13, 8.586062056093802e-15, -2.1748686983715528e-16, 5.509002826470406e-18, 0, 0, 0, 0]
#coeff_list = [0]*15




def bose_approx(x): 
        #b= x+5
        # f = sympy.utilities.lambdify(x,x+1)
        return x # f(x)

def bath(t):
    return bose_approx(t)


print(bose_approx(4))

def f(x):
    return numpy.exp(x)
#result = integrate.quad(f,-sp.inf,5)


