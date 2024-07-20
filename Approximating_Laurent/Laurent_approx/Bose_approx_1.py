from math import factorial
from sympy import symbols

#legacy version control of Bose_approx (old version) 


x= symbols('x')

# list with n=15 zeros
coeff_list =[0] * 15


a_0=1/12


def coeff(k, j) :
     if (k==0): 
          return a_0
     if(j==0): 
          return ( (2*k+1)/(2 * factorial(2*k+3)) + coeff(k, j+1))
     

     aux = coeff_list[j-1]/factorial(2*k+1 - 2*j)
     if(j>1) : 
          coeff_list.add()
          print(coeff_list)
          coeff_list[j-1] += aux 
          print(coeff_list)
     print(f"aux {aux}")
     return 0

print(coeff(1,0))


# bose implementt: 1/x + \frac{1}{2} + x \sum_{k=0}^{2N-1}
# index is here k-2 so i can get the two cases at the beginning included
# one could also start at -2 i don't know, or have an additional param 
def bose(N, index): 
    if(index==0):
          return 1/x + bose(N-1, index+1)
    if(index==1):
          return 1/2 + bose(N-1, index+1) 
    
    # implement: x \sum_{k=0}^{2N-1}
    aux = x * (coeff(index-2,0) * x**(2*(index-2)))
    print(aux)
    if(N-1==index-2):
         return aux
    else:
         return aux + bose(N, index+1)

print(bose(4,0))