import numpy as np

# Define the function based on the latest formula


def calculate_alpha(τ, γ, η):
    # Define the coefficients a_k
    n=10
    a_k = np.array([1/(k+1) for k in range(n+1)])  # Example coefficients, can be adjusted
    
    # Calculate the summation term
    sum_term = np.sum([a_k[k] * (-1)**(k+1) * γ**(2*k+1) for k in range(n+1)])
    
    # Calculate the main function
    alpha = np.exp(γ * τ) * η * (0.5 + (γ / 2) * sum_term)
    
    return alpha


def calculate_simplified_function(τ, n, g ):

    constant_term = 0.5 + (0.5 / 2) * (-0.0418)

    result = np.exp(0.5 * τ) * constant_term

    return result
def plot_debye(n,g) : 
    τ_values = np.arange(0.1, 10.0, 0.1)
    return [calculate_alpha(τ,1,1) for τ in τ_values]


#print(simplified_results)