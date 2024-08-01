import scipy.integrate as integrate
import scipy as sc
import numpy
import sympy 

import Bose_approx
#commit log:
#added zentral bath_front_factor
#added zentral distance_to_signularity 

x, y = sympy.symbols('x y')
#for the integral
lower_integral_limit = -50
upper_integral_limit = 50
number_laurent_terms = 3
distance_to_signularity = 0.01 
bath_front_faktor = 1/(numpy.pi)


#for the plot: 
step_size =0.1
number_of_steps = 10

start_table_string ="\\begin{array}{|c|c|c|}\hline\\textbf{Time} & \\textbf{Activity} & \\textbf{Duration} \\\\"
end_table_string = "\hline\end{array}"

def spectral_density(x): 
        return x/(x**2+1)

# bath function with closed bose 
def bose_closed(x): 
        return 1/(1-numpy.exp(-x))

def bath_integralfunction_closed(w,t):
        return spectral_density(w) * (bose_closed(w)-1) * numpy.exp((- (0+1j)*w*t))

def bath_closed(t) :
   result_1 = integrate.quad(bath_integralfunction_closed, lower_integral_limit, 0-distance_to_signularity,args=t)
   result_2 = integrate.quad(bath_integralfunction_closed, 0+distance_to_signularity, upper_integral_limit,args=t)
   return bath_front_faktor *(result_1[0]+result_2[0])

def bath_closed_verbose_integral_limits(t,lower_integral_limit, upper_integral_limit):
   result_1 = [0,0]#integrate.quad(bath_integralfunction_closed, lower_integral_limit, 0-distance_to_signularity,args=t)
   result_2 = integrate.quad(bath_integralfunction_closed, 0+distance_to_signularity, upper_integral_limit,args=t)
   return bath_front_faktor *(result_1[0]+result_2[0])  

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
   return bath_front_faktor*( result_1[0]+result_2[0])

def bath_approxed_verbose_integral_limits(t,lower_integral_limit, upper_integral_limit) :
   result_1 = integrate.quad(bath_integralfunction_approxed, lower_integral_limit, 0,args=t)
   result_2 = integrate.quad(bath_integralfunction_approxed, 0, upper_integral_limit,args=t)
   return bath_front_faktor* (result_1[0]+result_2[0])


def plot(function_to_plot) : 
    for i in range (1,number_of_steps):
        print(f"{float(i*step_size):.2f} & {float(function_to_plot(i*step_size)):.5f}\\\\")
    return 0


# Find out: How stabil is the inside integral with different upper and lower limits! 
number_of_steps=10
step_size = 100

def plot_integral_limits(t, integral_function_verbose_limits):
    for i in range (1,number_of_steps):
        # plotting integrals with different integration limits at the point t =1
        # discarding the imaginary part
        print(f"{float(t):.2f} & \\text{{integral limits:}} & {i*step_size} & {float(integral_function_verbose_limits(t,-i*step_size,i*step_size).real):.5f}\\\\")
    return 0     


def ploting_integral_limits_with_different_taus (k): 
    for i in range(1,k):
        print(f" \\text{{alpha({i})}} & & & \\\\")
        plot_integral_limits(i, bath_closed_verbose_integral_limits)
    #aktuell 10-100

print(start_table_string)
ploting_integral_limits_with_different_taus(5)
print(end_table_string)
def testing_simple_integral () :
    lower_integral_limit= -1000
    upper_integral_limit = 1
    distance_to_signularity = 0.01 

    result1 = integrate.quad(bose_closed, upper_integral_limit,0-distance_to_signularity)
    result2 = integrate.quad(bose_closed, 0+distance_to_signularity, upper_integral_limit) 
    print(result2)


