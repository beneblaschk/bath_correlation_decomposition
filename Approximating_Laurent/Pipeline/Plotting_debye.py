import numpy as np
import universal_plot

# Define the function based on the latest formula
coeff_list = [0.08333333333333333, -0.0013888888888888874, 3.3068783068782915e-05, -8.267195767195603e-07, 2.0876756987866386e-08, -5.284190138685735e-10, 1.3382536530666791e-11, -3.3896802963044296e-13, 8.586062056093802e-15, -2.1748686983715528e-16, 5.509002826470406e-18, 0, 0, 0, 0]


def calculate_alpha(τ, γ, η):
    # Define the coefficients a_k
    n=7
    a_k = np.array([1/(k+1) for k in range(n+1)])  # Example coefficients, can be adjusted
    a_k = coeff_list
    # Calculate the summation term
    sum_term = np.sum([a_k[k] * (-1)**(k+1) * γ**(2*k+1) for k in range(n+1)])
    # Calculate the main function
    alpha = np.exp(γ * τ) * η * (0.5 + (γ / 2) * sum_term)
    return alpha


def calculate_simplified_function(τ, n, g ):

    constant_term = 0.5 + (0.5 / 2) * (-0.0418)

    result = np.exp(0.5 * τ) * constant_term

    return result

def plot_debye(n,g):
    tau_range=[0]*3
    tau_range[0]=0.0
    tau_range[1]=5.0
    tau_range[2]=0.1
    return plot_debye_advanced_parameter(n,g,tau_range)

def plot_debye_advanced_parameter(n,g, tau_range) : 
    τ_values = np.arange(tau_range[0], tau_range[1],tau_range[2])
    return [calculate_alpha(τ,g,n) for τ in τ_values]

#for i in range(1,7):
#    print(plot_debye(1,i))


if __name__ == "__main__":
    
    #plot_debye(1,3)

    #calculate_alpha(2, 3, 1)
    universal_plot.show(plot_debye(1,3),[[0,'r']])

#print(simplified_results)