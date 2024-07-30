import scipy.integrate as integrate
import scipy as sc
import numpy
import sympy 

import Bose_approx
#x, y = sympy.symbols('x y')



#coeff_list = [0.08333333333333333, -0.0013888888888888874, 3.3068783068782915e-05, -8.267195767195603e-07, 2.0876756987866386e-08, -5.284190138685735e-10, 1.3382536530666791e-11, -3.3896802963044296e-13, 8.586062056093802e-15, -2.1748686983715528e-16, 5.509002826470406e-18, 0, 0, 0, 0]
#coeff_list = [0]*15






 # f = sympy.utilities.lambdify(x,x+1)

#def bath(t):
    #return bose_approx(t)


def bose_geschlossen(x): 
        return 1/(1-numpy.exp(-x))

def spectral_density(x): 
        return x/(x**2+1)

def bath_int(w,t):
        return spectral_density(w) * (bose_geschlossen(w)-1) * numpy.exp((- (0+1j)*w*t))


def bath(t) :
   result_1 = integrate.quad(bath_int, -50, 0,args=t)
   result_2 = integrate.quad(bath_int, 0, 50,args=t)
   return result_1[0]+result_2[0]

#print(bath(1))


def plot() : 
    for i in range (1,100):
        print(f"{float(i*0.1):.2f} & {float(bath(i*0.1)):.5f}\\\\")
    return 0

plot()
#print(bath(5))








    #def f(x):
    #return numpy.exp(x)

# for i in range (1,100):
#     k=i*1000
#     result = integrate.quad(bath_int, -k, 0)
#     print(f"{k}-0: {result[0]}")



# result = integrate.quad(bath_int, 0, sc.inf)
# print(result)