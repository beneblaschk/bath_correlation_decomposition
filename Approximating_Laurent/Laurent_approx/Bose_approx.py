from sympy import * 
#symbols, sin, lambdify, limit
import sympy as sp
from math import * 

x, y, z = symbols('x y z')

# Implementation from: Communication: Padé spectrum decomposition of Fermi function and Bose function

# reference function: 

f_ref = 1/ (1-sp.exp(-x)) 

a_0=1/12 

coeff_list = [0.08333333333333333, -0.0013888888888888874, 3.3068783068782915e-05, -8.267195767195603e-07, 2.0876756987866386e-08, -5.284190138685735e-10, 1.3382536530666791e-11, -3.3896802963044296e-13, 8.586062056093802e-15, -2.1748686983715528e-16, 5.509002826470406e-18, 0, 0, 0, 0]

# coeff implements \frac{2k+1}{2(2k+3)!} - \sum_{j=0}^{k-1} \frac{a_j}{(2k+1-2j)!} 
# implement 
# j is here j-1 to include the first term


# muss ich jetzt die coeff liste immer mit nehmen oder kann ich
# die einfach die global liste manipulieren? -> global

# the coeff function is called recursively until it matches the k
# because all k's before are also necessary for calculation

# to calculate the sum (second party) sum is a recursive function
# that iterates over all all a_j with increasing j, until it hits k-1 -> and 
# then when it is j==1 it terminates with 0 adding up everything before. 

# write now it prints out every part of a fraction to verify

def sum(k,j): 
     if (j==k):
          return 0
     aux = coeff_list[j]/factorial(2*k+1-2*j)
     print(f"   sum k:{k} j:{j}= {aux}")
     return aux + sum(k,j+1)


def coeff(k, k_index) :
     # when greater is than k than it should terminate
     if (k_index>k):
          return 0
     if (k_index==0): 
          coeff_list[0] = a_0
          return coeff(k, k_index+1) 

     aux1 =  (2*k_index+1)/(2 * factorial(2*k_index+3)) 
     print(f"part 1 of k: {k_index} = {aux1}")

     aux2 = sum(k_index,0)
     print(f"part 2 of k: {k_index} = {aux2}")
     coeff_list[k_index]=aux1 - aux2
     return coeff(k,k_index+1) 

#print(coeff(10,0))
#print(coeff_list)




# bose implementt: 1/x + \frac{1}{2} + x \sum_{k=0}^{2N-1}
# index is here k-2 so i can get the two cases at the beginning included
# one could also start at -2 i don't know, or have an additional param 
def bose(n, index,verbose): 
    if(index==0):
          if(verbose):
               print(f"bose({index}) of {n}", 1/x)
          return 1/x + bose(n, index+1,verbose)
    if(index==1):
          if(verbose): 
               print(f"bose({index}) of {n}", 1/2)
          return 1/2 + bose(n, index+1,verbose) 
    
    # implement:  \sum_{k=0}^{n} a_k x^{2k+1}
    # x wird in den Exponenten verschoben, index ist um zwei nach hinten verschoben
    aux = coeff_list[index-2]* x**(2*((index-2))+1)
    if(verbose):
     print(f"bose({index}) of {n}", aux)
    if(n-1==index):
         return aux
    else:
         return aux + bose(n, index+1,verbose)



#bose(1,0) und bose(2,0) funktionieren nicht!! 
f= f_ref
print("bose(11,0,true): Laurent series of Bose function with 3 terms")
h = bose(11,0,true)
print(f"Bose_approx: {h}")
# h = 1/x
# print(h)
# diff_list= [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

# print("configuration: ")
# print(f"Bose function")
# start = -10
# interval = 1
# for i in range(0,21): 
#     print(f"step: f({start+i*interval:.2f})") 
#     step = start+i*interval
#     if(step==0):
#          continue
#     laurent = (h.subs(x, step))
#     compare = f.subs(x, step) 
#     diff = laurent-compare
#     diff_list[i]=float(diff)
#     print(f"laurent : {float(laurent):.4f} reference: {float(compare):.4f} diff: {float(diff):.9f}")


#print(diff_list)
