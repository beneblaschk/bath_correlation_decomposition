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
for i in range(0,3): 
    n=10+i*5
    print(f"n={n}") 
    print(self_taylor(f,develop_point,n,0))


# selfbenchmark for num_execution times

self_taylor_n10 = timeit.timeit('self_taylor(f,develop_point,10,0)',
                               setup='from __main__ import self_taylor,f, degree, develop_point', 
                               number=num_executions)

self_taylor_n15 = timeit.timeit('self_taylor(f,develop_point,15,0)',
                               setup='from __main__ import self_taylor,f, degree, develop_point', 
                               number=num_executions)
self_taylor_n20 = timeit.timeit('self_taylor(f,develop_point,20,0)',
                               setup='from __main__ import self_taylor,f, degree, develop_point', 
                               number=num_executions)



print(f"Self implemented taylor with n=10 took {self_taylor_n10:.6f} seconds for {num_executions} executions.")
print(f"Self implemented taylor with n=15 took {self_taylor_n15:.6f} seconds for {num_executions} executions.")
print(f"Self implemented taylor with n=20 took {self_taylor_n20:.6f} seconds for {num_executions} executions.")

