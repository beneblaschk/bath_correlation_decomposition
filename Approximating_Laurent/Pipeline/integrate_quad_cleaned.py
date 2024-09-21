import scipy.integrate as integrate
import scipy as sc
import numpy
import sympy 
#git_upload

#import Bose_approx
#commit log:





x, y = sympy.symbols('x y')
#for the integral
lower_integral_limit = -16
upper_integral_limit = - lower_integral_limit
distance_to_signularity = 0.01
# 0.1 -> 0.05 -> 0.01 -> 0.005 -> 0.001 -> 0.0005 -> 0.0001
bath_front_faktor = 1/(numpy.pi)
#bath_front_faktor = 1
Omega = 0.4

start_table_string ="\\begin{array}{|c|c|}\\hline\\tau & \\alpha\\\\"
end_table_string = "\\hline\\end{array}"


def debye_sd (w) : 
      return 0.5 * (0.25*w)/(w**2+0.25**2)

def ohmic_sd (x) : 
      return numpy.pi*x*numpy.exp(-abs(x/Omega))

def ultra_violet_cutoff_sd (x) :
      #return numpy.exp(2) *x *(0.6 - x)
      return 0

# bath function with closed bose 
def bose_closed(x): 
        return 1/(1-numpy.exp(-x))

def bose_approxed(x):
        # changed to n=2 
        return 0.5 + 1/x

def bath_integralfunction(w,t,sd,approximated):
        if not approximated:
                return sd(w) * (bose_closed(w)) * numpy.exp(( (0+1j)*w*t))
        if approximated:
                return sd(w) * (bose_approxed(w)) * numpy.exp(( (0+1j)*w*t))
        return "Error"


def debye_simple_function(x): 
      return debye_sd(x)*bose_closed(x)

def bath(t, sd, approximated): 
        result_1 = integrate.quad(bath_integralfunction, lower_integral_limit, 0-distance_to_signularity,args=(t,sd,approximated))
        result_2 = integrate.quad(bath_integralfunction, 0+distance_to_signularity, upper_integral_limit,args=(t,sd,approximated))
        #i think i only need to integrate from 0 right??
        # i need to check wether the arguments are correctly transmitted
        
        return bath_front_faktor *(result_1[0]+result_2[0])

def bath_imag(t, sd, approximated): 
        result_1 = integrate.quad(bath_integralfunction, lower_integral_limit, 0-distance_to_signularity,args=(t,sd,approximated),complex_func=True)
        result_2 = integrate.quad(bath_integralfunction, 0+distance_to_signularity, upper_integral_limit,args=(t,sd,approximated),complex_func=True)
        #i think i only need to integrate from 0 right??
        # i need to check wether the arguments are correctly transmitted
        
        return bath_front_faktor *(result_1[0]+result_2[0])

def bath_simple(t): 
        result_1 = integrate.quad(debye_simple_function, lower_integral_limit, 0-distance_to_signularity)
        result_2 = integrate.quad(debye_simple_function, 0+distance_to_signularity, upper_integral_limit)
        
        return bath_front_faktor *(result_1[0]+result_2[0])

def bath_checking_singularities(t): 
        result_1 = integrate.quad(checking_singularites2, lower_integral_limit, 0-distance_to_signularity)
        result_2 = integrate.quad(checking_singularites2, 0+distance_to_signularity, upper_integral_limit)
        
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
      return [bath_imag(t,sd,approximated).imag for t in t_values]

def debye_simple_function(x): 
      return debye_sd(x)*bose_closed(x)

def checking_singularites (x) :
      return 1/(1-numpy.exp(x)) * 1 / (1+x**2)
def checking_singularites2 (x) :
      return 1/(1-numpy.exp(x)) * 1 / (1+x**2)*numpy.exp(-(1j)*x)

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
      #print('main')
      #integrate_quad_test(integrate_function,5)
        print("debye_closed_numerics_imag",end="=")

        print(bath_tau_set("debye", False, [0,30.1,1]))
        
        #print(bath_imag(1, debye_sd, False).imag)