from sympy import * 
#symbols, sin, lambdify, limit
import sympy as sp
from math import * 
# Origin: Taylor_approx_1_4 
# Now:  Laurent_approx_1_0 
# Now i want to try the implementation for the Laurent series solved with the residual theorem

# Define the symbolic variable
x, y, z, a, z_0 = symbols('x y z a z_0')

# Define the symbolic function

#  function 
f = 1/(x*(x-1))


def laurent(f, pol) : 
    # iterating over all poles
    g = 0
    res = [0, len(pol)]
    for i in range(0,len(pol)):
        print('pol:')
        print(pol[i])
        #z_0 is the next pol
        z_0= pol[i] 
        #f now only contains z 
        f= f.subs(x,z) 
        # the residual is calculated like: 
        res[i] = limit(f*(z-z_0),z,z_0) 
        print('residual',i)
        print(res[i]) 
        g = g + res[i]*(z-z_0)**i
    return g


# Now we are testing the limits:
# the pol is at 0 
z_0 = 0

# we are using z now 
f= f.subs(x,z) 
print(f)

print(limit(f*(z-z_0),z,z_0))

# the pol ist now at 1 

z_0= 1
print('pol is at 1:')
print(limit(f*(z-z_0),z , z_0))
# Res(f, z_0) = lim_{z -> z_0} (z-z_0) f(z) = lim_{z -> 1} (z-1) 1/(z*(z-1) = lim_{z-> 1} z/z*(z-1) = 1 




#print(limit(f, x,z_0))

# we look at z=0 now 
# f has a single pol at z_0=0
# Res(f, z_0) = lim_{z -> z_0} (z-z_0) f(z) = lim_{z -> 0} (z-0) 1/(z*(z-1) = lim_{z-> 0} z/z*(z-1) = -1 
# 



 
def taylor(f, a, terms, index) : 
    if terms==0:
        print("final: ")
        return f.subs(x,a)/factorial(index)*((x-a)**(index))
    aux = f.subs(x,a)/factorial(index)*((x-a)**(index)) 
    print(aux)
    return aux + taylor(f.diff(x),a,terms-1, index+1)



print(laurent(f,a,[0,1]))
