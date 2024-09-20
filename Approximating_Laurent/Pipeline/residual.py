import numpy
import universal_plot
#git_upload

im = 1j

T = 1

gamma=0.25
eta = 0.5
Omega = 0.4
n= 5 # for laurent approx
K= 5 # for Matsubara terms (imaginary poles are periodically)

#pre calculated values of the laurent approx
a = [0.08333333333333333, -0.0013888888888888874, 3.3068783068782915e-05, -8.267195767195603e-07, 2.0876756987866386e-08,-5.284190138685735e-10]#, 1.3382536530666791e-11, -3.3896802963044296e-13, 8.586062056093802e-15, -2.1748686983715528e-16, 5.509002826470406e-18, 0, 0, 0, 0]

def residual_debye_closed(t):
    k_values = numpy.arange(K+1)
    #return 4 * numpy.exp(2*t) - (numpy.sum( (2*numpy.pi*k_values)/(1-(2*numpy.pi*k_values)**2) *numpy.exp(-2*numpy.pi * k_values* t)))
    # new valuse
    #return numpy.sum(1 / k_values) * numpy.exp(-2*numpy.pi * k_values*t)
    return numpy.sum(eta * (4 * numpy.pi*k_values* gamma)/(4 * numpy.pi**2* k_values**2+gamma**2) * numpy.exp(-2*numpy.pi* k_values*t))
        
def residual_debye_closed_first_term(t):

    k_values = numpy.arange(K+1)
    return 1j* eta* gamma* (1/(1-numpy.exp(-(1j*gamma)/T)))*numpy.exp(-gamma*t)+numpy.sum(eta * (4 * numpy.pi*k_values* gamma)/(4 * numpy.pi**2* k_values**2+gamma**2) * numpy.exp(-2*numpy.pi* k_values*t))       

def residuals_bose_first_term (t):
    # test
    return 1/8 * 1/numpy.sin(gamma) * numpy.exp(-gamma*t) 

def residual_debye_closed_simplified(t):
    k_values = numpy.arange(K+1)
    return 2 - numpy.sum(2*numpy.pi*k_values)/(1-(2*numpy.pi*k_values)**2)


def residual_debye_laurent(t):
    k_values = numpy.arange(n+1)
    return numpy.exp(gamma*t)*eta*(0.5*gamma/2*numpy.sum(a * ((-1)**(k_values+1))*(gamma**(2*k_values)+1)))

def residual_ohmic_closed(t):
    k_values = numpy.arange(K+1)
    return -4 * numpy.pi**2 * numpy.sum(k_values*numpy.exp((-2*numpy.pi*k_values*t) - 1j *(2*numpy.pi*k_values)/Omega))

def residual_singualarity_check(t): 
    k_values = numpy.arange(1,K+1)
    print('singu')
    return numpy.sum(1/(k_values)**3 * numpy.exp(1)**(-2*numpy.pi * k_values))


def residual_singualartiy_check2(t):
    k_values = numpy.arange(1,K+1)
    print('singu2')
    return numpy.sum(1/(k_values) * numpy.exp(-2*numpy.pi * k_values))


def bath(t,sd,approximated):
    #calcaltor = residual_laurent
    # currently we only have the debye 
    if sd=="ohmic":
        if approximated: 
            print("not possible here")
        else:
            calculator = residual_ohmic_closed
 
        return calculator(t)
    if sd=="debybe_simple":
        calculator = residual_debye_closed_simplified
    if sd=="singularity_check":
        print('singu1')
        calculator = residual_singualarity_check
    if sd=="singularity_check2":
        print('singu2')
        calculator = residual_singualartiy_check2
    if sd=="debye_first_term":
        calculator = residual_debye_closed_first_term

    if sd=="debye":
        if approximated: 
            calculator = residual_debye_laurent
        else:
            calculator = residual_debye_closed

    
    return calculator(t)




def calculate_bath_tau_set(sd, approximated, tau_range):
    """
    sd: spectral density 
    debye - ohmic - ultra_violet_cutoff
    approximated: True Laurent, False closed
    """
    t_values = numpy.arange(tau_range[0], tau_range[1],tau_range[2])
    return [bath(t,sd,approximated).real for t in t_values] 

if __name__ == "__main__":
    print("debye_closed_residuals",end="=")
    #print(residual_debye_closed_first_term(0))
    print(calculate_bath_tau_set("debye_first_term", False, [0,30.1,1]))
