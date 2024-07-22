import matplotlib.pyplot as plt

# Given coefficients
numbers = [0.08333333333333333, -0.0013888888888888874, 3.3068783068782915e-05, -8.267195767195603e-07, 
                2.0876756987866386e-08, -5.284190138685735e-10, 1.3382536530666791e-11, -3.3896802963044296e-13, 
                8.586062056093802e-15, -2.1748686983715528e-16, 5.509002826470406e-18]

# Coefficient indices
indices = list(range(len(numbers)))

# Plotting
# Plotting the numbers with a logarithmic scale on the y-axis
plt.figure(figsize=(10, 5))
plt.plot(numbers, marker='o', linestyle='-')
plt.yscale('log')
plt.title('Plot of Given List of Numbers (Logarithmic Scale)')
plt.xlabel('k')
plt.ylabel('a_k Value (Log Scale)')
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.show()
