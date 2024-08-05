import scipy.integrate as integrate
import scipy as sc
import numpy
import sympy 

import Bose_approx
#commit log:
# made the step size and the number of steps only zentral 

x, y = sympy.symbols('x y')
#for the integral
lower_integral_limit = -50
upper_integral_limit = 50
number_laurent_terms = 3
distance_to_signularity = 0.01 
# bath_front_faktor = 1/(numpy.pi)
bath_front_faktor = 1


#for the plot: 
number_of_steps= 10
step_size = 100

start_table_string ="\\begin{array}{|c|c|c|}\\hline\\textbf{Time} & \\textbf{Activity} & \\textbf{Duration} \\\\"
end_table_string = "\\hline\\end{array}"

def spectral_density(x): 
        return x/(x**2+1)

# bath function with closed bose 
def bose_closed(x): 
        return 1/(1-numpy.exp(-x))

def bose_closed_with_decoy_tau(x,t): 
        return 1/(1-numpy.exp(-x))

def bath_integralfunction_closed(w,t):
        return spectral_density(w) * (bose_closed(w)-1) * numpy.exp((- (0+1j)*w*t))


def bose_closed_verbose_integral_limits(t, lower_integral_limit, upper_integral_limit, only_positive_integral) :
    result_1 = [0,0]
    if not only_positive_integral:
        result_1 = integrate.quad(bose_closed_with_decoy_tau, lower_integral_limit, 0-distance_to_signularity,args=t)
    result_2 = integrate.quad(bose_closed_with_decoy_tau, 0+distance_to_signularity, upper_integral_limit,args=t)
    return bath_front_faktor *(result_1[0]+result_2[0])



def bath_closed(t) :
   result_1 = integrate.quad(bath_integralfunction_closed, lower_integral_limit, 0-distance_to_signularity,args=t)
   result_2 = integrate.quad(bath_integralfunction_closed, 0+distance_to_signularity, upper_integral_limit,args=t)
   return bath_front_faktor *(result_1[0]+result_2[0])



def bath_closed_verbose_integral_limits(t,lower_integral_limit, upper_integral_limit, only_positive_integral):
   result_1 = [0,0]
   if not only_positive_integral:
        result_1 = integrate.quad(bath_integralfunction_closed, lower_integral_limit, 0-distance_to_signularity,args=t)
   result_2 = integrate.quad(bath_integralfunction_closed, 0+distance_to_signularity, upper_integral_limit,args=t)
   return bath_front_faktor *(result_1[0]+result_2[0])  

# bath function with approxed bose 
def transform_symbolic_to_callable(f) : 
    f = sympy.utilities.lambdify(x,f)
    return f

def bose_approxed(): 
        h= Bose_approx.bose(number_laurent_terms,x)
        return transform_symbolic_to_callable(h)

def bose_approxed_with_decoy_tau(x,t): 
        x, y, z = sympy.symbols('x y z')
        h= Bose_approx.bose(number_laurent_terms,x)
        return transform_symbolic_to_callable(h)


def bose_approxed_with_decoy_tau_manual(x,t):
        # changed to n=2 
        return 0.5 + 1/x

def bose_approxed_verbose_integral_limits(t, lower_integral_limit, upper_integral_limit, only_positive_integral) :
    result_1 = [0,0]
    if not only_positive_integral:
        result_1 = integrate.quad(bose_approxed_with_decoy_tau_manual, lower_integral_limit, 0-distance_to_signularity,args=t)
    result_2 = integrate.quad(bose_approxed_with_decoy_tau_manual, 0+distance_to_signularity, upper_integral_limit,args=t)
    return bath_front_faktor *(result_1[0]+result_2[0])


def bath_integralfunction_approxed(w,t):
        return spectral_density(w) * (bose_approxed()(w)-1) * numpy.exp((- (0+1j)*w*t))

def bath_approxed(t) :
   result_1 = integrate.quad(bath_integralfunction_approxed, lower_integral_limit, 0,args=t)
   result_2 = integrate.quad(bath_integralfunction_approxed, 0, upper_integral_limit,args=t)
   return bath_front_faktor*( result_1[0]+result_2[0])

def bath_approxed_verbose_integral_limits(t,lower_integral_limit, upper_integral_limit, only_positiv_integral) :
   result_1 = [0,0]
   if not only_positiv_integral:
        result_1 = integrate.quad(bath_integralfunction_approxed, lower_integral_limit, 0,args=t)
   result_2 = integrate.quad(bath_integralfunction_approxed, 0, upper_integral_limit,args=t)
   return bath_front_faktor* (result_1[0]+result_2[0])


def plot(function_to_plot) : 
    for i in range (1,number_of_steps):
        print(f"{float(i*step_size):.2f} & {float(function_to_plot(i*step_size)):.1f}\\\\")
    return 0


def plot_integral_limits(t, integral_function_verbose_limits, only_positiv_integral):
    for i in range (1,number_of_steps):
        # plotting integrals with different integration limits at the point t =1
        # discarding the imaginary part
        print(f"{float(t):.0f} & \\text{{limit:}} & {i*step_size} & {float(integral_function_verbose_limits(t,-i*step_size,i*step_size,only_positiv_integral).real):.0f}\\\\")
    return 0     


def ploting_integral_limits_with_different_taus (k,function_integrated_verbose_integral_limits, only_positiv_integral): 
    for i in range(1,k):
        print(f" \\text{{alpha({i})}} & & & \\\\")
        plot_integral_limits(i, function_integrated_verbose_integral_limits,only_positiv_integral)
    #aktuell 10-100


def plot_bose (): 
    print(start_table_string)
    ploting_integral_limits_with_different_taus(2,bose_approxed_verbose_integral_limits,True)
    print(end_table_string)


plot_bose()


def testing_simple_integral () :
    lower_integral_limit= -1000
    upper_integral_limit = 1
    distance_to_signularity = 0.01 

    result1 = integrate.quad(bose_closed, upper_integral_limit,0-distance_to_signularity)
    result2 = integrate.quad(bose_closed, 0+distance_to_signularity, upper_integral_limit) 
    print(result2)


