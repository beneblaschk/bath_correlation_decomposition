from sympy import symbols, sin, lambdify

# Define the variable
x = symbols('x')

# Define the function
f = x **2

def taylor(h, a, x): 
    return h(a)

print(taylor(f, 2,0))

# Differentiate the function
f_prime = f.diff(x)

# Convert to a numerical function
f_prime_lambdified = lambdify(x, f_prime)

# Test the numerical function
print(f_prime_lambdified(2))  # Evaluate the derivative at x=1
