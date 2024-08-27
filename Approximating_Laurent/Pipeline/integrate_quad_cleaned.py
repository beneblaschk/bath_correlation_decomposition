import scipy.integrate as integrate
import scipy as sc
import numpy
import sympy 
#git_upload

#import Bose_approx
#commit log:





x, y = sympy.symbols('x y')
#for the integral
lower_integral_limit = -200
upper_integral_limit = - lower_integral_limit
distance_to_signularity = 0.01 
bath_front_faktor = 1/(numpy.pi)
#bath_front_faktor = 1


start_table_string ="\\begin{array}{|c|c|}\\hline\\tau & \\alpha\\\\"
end_table_string = "\\hline\\end{array}"


def debye_sd (x) : 
      return x/(x**2+1)

def ohmic_sd (x) : 
      return numpy.pi*x*numpy.exp(-x/5)

def ultra_violet_cutoff_sd (x) :
      return pow(numpy.exp(1),2) *x *(2 - x)

# bath function with closed bose 
def bose_closed(x): 
        return 1/(1-numpy.exp(-x))

def bose_approxed(x):
        # changed to n=2 
        return 0.5 + 1/x

def bath_integralfunction(w,t,sd,approximated):
        if not approximated:
                return sd(w) * (bose_closed(w)-1) * numpy.exp((- (0+1j)*w*t))
        if approximated:
                return sd(w) * (bose_approxed(w)-1) * numpy.exp((- (0+1j)*w*t))
        return "Error"


def debye_simple_function(x): 
      return debye_sd(x)*bose_closed(x)

def bath(t, sd, approximated): 
        result_1 = integrate.quad(bath_integralfunction, lower_integral_limit, 0-distance_to_signularity,args=(t,sd,approximated))
        result_2 = integrate.quad(bath_integralfunction, 0+distance_to_signularity, upper_integral_limit,args=(t,sd,approximated))
        #i think i only need to integrate from 0 right??
        # i need to check wether the arguments are correctly transmitted
        
        return bath_front_faktor *(result_1[0]+result_2[0])


def bath_simple(t): 
        result_1 = integrate.quad(debye_simple_function, lower_integral_limit, 0-distance_to_signularity)
        result_2 = integrate.quad(debye_simple_function, 0+distance_to_signularity, upper_integral_limit)
        
        return bath_front_faktor *(result_1[0]+result_2[0])

def bath_tau_set(sd,approximated,tau_range):
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
      return [bath(t,sd,approximated) for t in t_values]

def debye_simple_function(x): 
      return debye_sd(x)*bose_closed(x)

def integrate_function(x): 
   return 1/(1+x**2)

def integrate_quad_test(function, steps):
        for i in range(1,steps):
                a = i
                result = integrate.quad(function, a*lower_integral_limit, a*upper_integral_limit)
                print("limits:",upper_integral_limit* a,"res: :",result) 
        result = integrate.quad(function, -sc.inf, sc.inf)
        print("infinify", "res: :",result)
        print("pi compare      ", sc.pi)

def integrate_sampling(function,steps):
        '''
        dont go further than 10**8 it will crash
        '''
        for i in range(1,steps):
                x = numpy.arange(-10**i,10**i)
                y1 = function(x)
                I1 = integrate.simpson(y1, x=x)
                print("limits: 10**",i,": ",(10**i),I1)

if __name__ == "__main__":
      print('main')
      #integrate_quad_test(integrate_function,5)

      print(bath_simple(1))