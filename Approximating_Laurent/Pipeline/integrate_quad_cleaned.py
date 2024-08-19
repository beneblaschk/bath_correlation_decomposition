import scipy.integrate as integrate
import scipy as sc
import numpy
import sympy 
#git_upload

#import Bose_approx
#commit log:
# now we want to do closed and approxed together! 

x, y = sympy.symbols('x y')
#for the integral
lower_integral_limit = -100
upper_integral_limit = - lower_integral_limit
distance_to_signularity = 0.01 
bath_front_faktor = 1/(numpy.pi)
#bath_front_faktor = 1


#for the plot: 
number_of_steps= 100
step_size = 0.1

start_table_string ="\\begin{array}{|c|c|}\\hline\\tau & \\alpha\\\\"
end_table_string = "\\hline\\end{array}"


def debye_sd (x) : 
      return x/(x**2+1)

def ohmic_sd (x) : 
      return numpy.pi*x*numpy.exp(-x/5)

def ultra_violet_cutoff_sd (x) :
      return pow(numpy.exp(1),2) *x *(2 - x)

def spectral_density(x): 
        return x/(x**2+1)

# bath function with closed bose 
def bose_closed(x): 
        return 1/(1-numpy.exp(-x))

def bath_integralfunction_closed(w,t):
        return spectral_density(w) * (bose_closed(w)-1) * numpy.exp((- (0+1j)*w*t))

def bath_integralfunction_closed_sd_select(w,t,sd):
        return sd(w) * (bose_closed(w)-1) * numpy.exp((- (0+1j)*w*t))

def bath_closed(t) :
   result_1 = integrate.quad(bath_integralfunction_closed, lower_integral_limit, 0-distance_to_signularity,args=t)
   result_2 = integrate.quad(bath_integralfunction_closed, 0+distance_to_signularity, upper_integral_limit,args=t)
   return bath_front_faktor *(result_1[0]+result_2[0])

def bath_closed_sd_select(t, sd): 
        result_1 = integrate.quad(bath_integralfunction_closed_sd_select, lower_integral_limit, 0-distance_to_signularity,args=(t,sd))
        result_2 = integrate.quad(bath_integralfunction_closed_sd_select, 0+distance_to_signularity, upper_integral_limit,args=(t,sd))
        #i think i only need to integrate from 0 right??
        # i need to check wether the arguments are correctly transmitted
        
        return bath_front_faktor *(result_1[0]+result_2[0])


def bath_closed_tau_set(eta,gamma,tau_range):
      t_values = numpy.arange(tau_range[0], tau_range[1],tau_range[2])
      return [bath_closed(t) for t in t_values]

def bath_closed_tau_set_sd_select(sd,tau_range):
      """
      numerical approximated bath 
      sd: spectral density 
      debye - ohmic - ultra_violet_cutoff
      """
      if sd=="debye":
        sd = debye_sd
      if sd=="ohmic":
        sd = ohmic_sd
      if sd=="ultra_violet_cutoff":
        sd = ultra_violet_cutoff_sd


      t_values = numpy.arange(tau_range[0], tau_range[1],tau_range[2])
      return [bath_closed_sd_select(t,sd) for t in t_values]



def plot(function_to_plot) : 
    print(start_table_string)
    for i in range (1,number_of_steps):
        print(f"{float(i*step_size):.2f} & {float(function_to_plot(i*step_size)):.4f}\\\\")
    print(end_table_string)
    return 0

def bath_integralfunction_closed_fixed(w):
        return spectral_density(w) * (bose_closed(w)-1) * numpy.exp((- (0+1j)*w*2))
if __name__ == "__main__":
        plot(bath_closed)
