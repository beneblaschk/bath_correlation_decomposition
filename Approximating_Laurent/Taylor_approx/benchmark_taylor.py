import timeit
import scipy

# imports for self_implement
from math import factorial
from sympy import symbols, exp 

x = symbols('x')
a = symbols('a')

# import for lib function
from scipy.interpolate import approximate_taylor_polynomial
import numpy as np


# symbolic function 
#f = x**5
#f= x**5
f = 1/exp(x) 

# library input
def g(x): 
    #return np.exp(x)
    #return x**5
    return 1/np.exp(x)

degree = 30

probe = 5

develop_point = 0

# Number of executions for the benchmark
num_executions = 1000
def self_taylor(f, a, terms, index) : 
    if terms==0:
        return f.subs(x,a)/factorial(index)*((x-a)**(index))
    aux = f.subs(x,a)/factorial(index)*((x-a)**(index)) 
    return aux + self_taylor(f.diff(x),a,terms-1, index+1)


# calculate test 
self_taylor_approx= (self_taylor(f,develop_point,degree,0))
# print out polynom 
print('testing self programmed: ')
print(self_taylor_approx)
# print out at probe 
print(self_taylor_approx.subs(x,probe))

# selfbenchmark for num_execution times

self_taylor_time = timeit.timeit('self_taylor(f,develop_point,degree,0)',
                               setup='from __main__ import self_taylor,f, degree, develop_point', 
                               number=num_executions)



# calculate test 
lib_approx = approximate_taylor_polynomial(g,develop_point,degree,degree+2)
print('testing lib function: ')
print(lib_approx)
print(lib_approx(probe))
lib_taylor_time = timeit.timeit('scipy.interpolate.approximate_taylor_polynomial(g,develop_point,degree,degree+2)',
                               setup='from __main__ import g, develop_point, degree, scipy',
                               number=num_executions)


print(f"Self implemented taylor took {self_taylor_time:.6f} seconds for {num_executions} executions.")
print(f"lib function     taylor took {lib_taylor_time:.6f} seconds for {num_executions} executions.")

