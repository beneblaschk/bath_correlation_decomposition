import numpy
import universal_plot
#git_upload

gamma=1
eta = 1
n= 5 # for laurent approx
K= 5 # for Matsubara terms (imaginary poles are periodically)

#pre calculated values of the laurent approx
a = [0.08333333333333333, -0.0013888888888888874, 3.3068783068782915e-05, -8.267195767195603e-07, 2.0876756987866386e-08,-5.284190138685735e-10]#, 1.3382536530666791e-11, -3.3896802963044296e-13, 8.586062056093802e-15, -2.1748686983715528e-16, 5.509002826470406e-18, 0, 0, 0, 0]

def residual_debye_closed(t):
    k_values = numpy.arange(n+1)
    return 4 * numpy.exp(2*t) - (numpy.sum( (2*numpy.pi*k_values)/(1-(2*numpy.pi*k_values)**2) *numpy.exp(2*numpy.pi * k_values* t)))

def residual_debye_laurent(t):
    k_values = numpy.arange(n+1)
    return numpy.exp(gamma*t)*eta*(0.5*gamma/2*numpy.sum(a * ((-1)**(k_values+1))*(gamma**(2*k_values)+1)))

def bath(t,sd,approximated):
    #calcaltor = residual_laurent
    # currently we only have the debye 
    if approximated: 
        calcultor = residual_debye_laurent
    else:
        calcultor = residual_debye_closed

    
    return calcultor(t)




def calculate_bath_tau_set(sd, approximated, tau_range):
    """
    sd: spectral density 
    debye - ohmic - ultra_violet_cutoff
    approximated: True Laurent, False closed
    """
    t_values = numpy.arange(tau_range[0], tau_range[1],tau_range[2])
    return [bath(t,sd,approximated) for t in t_values] 

if __name__ == "__main__":
    print("main")
     #print(bath(1,"debye",False))
    print(calculate_bath_tau_set("debye",False,[0,1,0.5]))