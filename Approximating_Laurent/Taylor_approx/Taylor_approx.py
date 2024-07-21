a = 1

x= 6

def f(x):
    return x**2
def f1(x):
    return 2*x
def f2(x): 
    return 2

def tay(h,h1,h2, a,x):
    return h(a) + h1(a)*(x-a) + h2(a)/2 *(x-a)**2 


print(tay(f,f1,f2,a,x))


# approximate a simple function x^2 

# x^2 at the point x=5 
# the series is developed at the point (1,0) or (0,0) 

# f(x) = f(a) + \frac{f'(a)}{1} (x-a) + \frac{f"(a)}{2}(x-a)^2

a= 0
# f(0) = 0
# f'(x) = 2x
# f'(0) = 0
# f"(x) = 2
# f"(0) = 2

# f(5) = f(0) + \frac{0}{1}( 5-1) + \frac{2}{2} (5)^2

# f(5) =  0 + 0 + 25 
# compute f(5) 
print((0)^2 + 0*(4)+ (5)^2)

# now with the develop point (0,1)

# f(1) = 1
# f'(x) = 2x
# f'(1) = 2
# f"(x) = 2
# f"(1) = 2

# f(5) = f(1) + \frac{2}{1}( 5-1) + \frac{2}{2} (5-1)^2

# f(5) = 1 + 8 + 16 = 25 



