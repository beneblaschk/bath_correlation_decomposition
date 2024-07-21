from sympy import symbols, sin, lambdify

# Define the symbolic variable
x = symbols('x')
a = symbols('a')

# Define the symbolic function
f = x **2 

# Differentiate the function
f_prime = f.diff(x)

# Evaluate the original function at x = 1 using subs and evalf
f_value_at_1 = f.subs(x, 5)
#print(f_value_at_1)

print(f.diff(x))
print(f.diff(x).subs(x,6))
print(f.diff(x).diff(x))
print(f.diff(x).diff(x).subs(x,6))

def taylor(f, a, y) : 
    f1 = f.diff(x)
    f2 = f1.diff(x)
    return f.subs(x,a)+f1.subs(x,a)*(y-a)+f2.subs(x,a)/2 *(y-a)**2


#print(taylor(f,0, 3)) 

# mabye one could make it iteratevily, to continue calling until all the derivates are done