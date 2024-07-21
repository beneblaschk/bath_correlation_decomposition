from scipy.interpolate import approximate_taylor_polynomial
import numpy as np



def g(x): 
    return 1/np.exp(x)
degree=20
develop_point = 0
probe = 7

lib_approx = approximate_taylor_polynomial(g,develop_point,degree, probe+3)

print(lib_approx) 
print(lib_approx(probe))