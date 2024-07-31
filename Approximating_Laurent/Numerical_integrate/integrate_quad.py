import scipy.integrate as integrate
import scipy as sc
import numpy
import sympy 

import Bose_approx
x, y = sympy.symbols('x y')
lower_integral_limit = -50
upper_integral_limit = 50
number_laurent_terms = 3
#for the plot: 
step_size =0.1
number_of_steps = 10

def spectral_density(x): 
        return x/(x**2+1)

# bath function with closed bose 
def bose_closed(x): 
        return 1/(1-numpy.exp(-x))

def bath_integralfunction_closed(w,t):
        return spectral_density(w) * (bose_closed(w)-1) * numpy.exp((- (0+1j)*w*t))

def bath_closed(t) :
   result_1 = integrate.quad(bath_integralfunction_closed, lower_integral_limit, 0,args=t)
   result_2 = integrate.quad(bath_integralfunction_closed, 0, upper_integral_limit,args=t)
   return (1/2j) *(result_1[0]+result_2[0])

# bath function with approxed bose 
def transform_symbolic_to_callable(f) : 
    f = sympy.utilities.lambdify(x,f)
    return f

def bose_approxed(): 
        h= Bose_approx.bose(number_laurent_terms,x)
        return transform_symbolic_to_callable(h)

def bath_integralfunction_approxed(w,t):
        return spectral_density(w) * (bose_approxed()(w)-1) * numpy.exp((- (0+1j)*w*t))

def bath_approxed(t) :
   result_1 = integrate.quad(bath_integralfunction_approxed, lower_integral_limit, 0,args=t)
   result_2 = integrate.quad(bath_integralfunction_approxed, 0, upper_integral_limit,args=t)
   return result_1[0]+result_2[0]

def bath_approxed_verbose_limits(t,lower_integral_limit, upper_integral_limit) :
   result_1 = integrate.quad(bath_integralfunction_approxed, lower_integral_limit, 0,args=t)
   result_2 = integrate.quad(bath_integralfunction_approxed, 0, upper_integral_limit,args=t)
   return result_1[0]+result_2[0]


def plot(function_to_plot) : 
    for i in range (1,number_of_steps):
        print(f"{float(i*step_size):.2f} & {float(function_to_plot(i*step_size)):.5f}\\\\")
    return 0


# Find out: How stabil is the inside integral with different upper and lower limits! 
number_of_steps=10
step_size = 10

def plot_integral_limits():
    for i in range (1,number_of_steps):
        print(f"{float(1):.2f} & integral limits: & {i*step_size} & {float(bath_approxed_verbose_limits(1,-i*step_size,i*step_size)):.5f}\\\\")
    return 0     

plot_integral_limits()
