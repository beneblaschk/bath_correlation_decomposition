import matplotlib.pyplot as plt
import Parser_table_to_list as parser
import Plotting_debye as deb_plot
import numpy as np
import universal_plot
import math
import integrate_quad_cleaned
import sys
import residual
#git_upload

#commit: 
 

sd_array = [0]*3
sd_array[0] = "debye"
sd_array[1] = "ohmic"
sd_array[2] = "ultra_violet_cutoff"


def format(compare,spectral_density,bose,integral):
    """
    input: configuration
    compare: what is compared
    spectral_density: which one is used: debye
    bose: laurent - closed? -taylor? 
    integral: residual - numerical
    """
    tau_range = [0]*3 
    tau_range[0] = 0.0
    tau_range[1] = 30 
    tau_range[2] = 1

    parameter_range = []
    parameter_range.append([])
    parameter_range[0] = [0]*3
    parameter_range[0][0] = 1 # eta = 1

    parameter_range.append([])
    parameter_range[1] = [0]*3

    parameter_range[1][0] = 1 # gamma =0,10.0, 0.1
    parameter_range[1][1] = 4
    parameter_range[1][2] = 0.5

    if len(sys.argv)>1:
        verbose= int(sys.argv[1])
    else:
        verbose = 0

    # mabye könnte man hier auch eine liste von attributen machen
    # empty_data set, alpha_values usw. 
    format_advanced_parameter(compare,spectral_density,bose,integral,tau_range, parameter_range,verbose)


def format_advanced_parameter(compare, spectral_density, bose, integral, tau_range, parameter_range, config):
    """
    input: configuration
    compare: what is compared
    spectral_density: which one is used: debye
    bose: laurent - closed? -taylor? 
    integral: residual - numerical
    tau_range (start,end, step-size)
    parametere_range (start, end, step-size) []
    verbose output possible
    number of graphs and parameters
    config == 0 > no output
    config == 1 > limited parameter output
    """
    # verbose configurations: 
    # 0 nichts
    # 1 limited 
    # 2 full verbose
    verbose = False

    if config == 1: 
        print(f"tau: {tau_range[0]},{tau_range[1]},{tau_range[2]}") 
        print(f"gamma: {parameter_range[1][0]},{parameter_range[1][1]}, {parameter_range[1][2]}")
    
    if config==2:
        verbose = True


    # Tau Werte 
    tau_range[1] = tau_range[1] +tau_range[2]  # added one element because numpy.arrange always exclude the endpoint

    tau_start = tau_range[0]
    tau_end = tau_range[1]
    tau_step_size = tau_range[2]
    if verbose:
        print(f"tau values: from {tau_range[0]} to {tau_range[1]} in {tau_range[2]} steps")

       # hier werden die tau-Werte eingespeist
    
    data_set = [[round(i, 1)] for i in np.arange(tau_start,tau_end, tau_step_size)]

    number_of_datapoints = len(data_set)# ((tau_end-tau_start)/tau_step_size)
    if verbose:
        print(f"empty data_set: \n {data_set}")
        print(f"resulting in {number_of_datapoints} number of datapoints")
    if verbose:
        print(f"gamma values: from {parameter_range[1][0]} to {parameter_range[1][1]} in {parameter_range[1][2]} steps")


    # We have 3 configurations:
    # spectral density: debye, ohmic, ultraviolet 
    # bose: closed, laurent
    # integral: residual - numerical 

    # compare: 
    # spectral density: 3 number of graphs! 
    # bose: closed, laurent: 2 number of graphs! 
    # integral: residual - numerical: 2 number of graphs! 

    # one is compare, the rest is fixed! 


    # labels 
    number_of_graphs=3
    sd_array = [0]*3
    sd_array[0] = "debye"
    sd_array[1] = "ohmic"
    sd_array[2] = "ultra_violet_cutoff"

    label = [['',''],['','']]
    if bose=='compare':
        label= [["closed",''],["approximated",'']]
    if integral=="residual":
        label= [[f"{spectral_density} {bose} {integral}",'']]

    if spectral_density=="compare":
        label = [['',''],['',''],['','']]
        number_of_graphs =3
        print("number of graphs: 3 ")
        for i in range(0,number_of_graphs):
            label[i] = [f"{sd_array[i]} {bose} {integral}",'']
    
    if bose=="compare": 
        number_of_graphs = 2
        print("number of graphs: 2 ")
        for i in range(1,number_of_graphs):
            label[0] = [f"{spectral_density} closed {integral}",'']
            label[1] = [f"{spectral_density} laurent {integral}",'']
            break
    
    if integral=="compare":
        number_of_graphs = 2
        print("number of graphs: 2 ")
        for i in range(0,number_of_graphs):
            label[0] = [f"{spectral_density} {bose} numerical",'']
            label[1] = [f"{spectral_density} {bose} residual",'']
            print(i)
            break
    # here the number of graphs is cleared!

    sd = spectral_density # mabye also the array
    # the spectral density will be given in the big loop

    if bose=='closed':
        approximated = False
    else:
        approximated=True

    if integral=="residual":
        calculator_function= residual.calculate_bath_tau_set

    if integral=="numerical":
        calculator_function= integrate_quad_cleaned.bath_tau_set
    




    if verbose:
        print(f"resulting in {number_of_graphs} graphs")

    # now the calculator function is applied
    alpha_values = [0]*number_of_graphs

    # here is the main allocation !
    for i in range (0, number_of_graphs):
        # first we check for the spectral density compare! 
        if spectral_density=="compare":
            # here we are also iterating over the spectral density array 
            alpha_values[i]= calculator_function(sd_array[i],approximated,tau_range)
            continue
        if bose=="compare":
            alpha_values[i]= calculator_function(sd,not (i%2==0),tau_range)  
            continue
        # now only the intgral compare is left! 

        if integral=="compare":
            alpha_values[0] = integrate_quad_cleaned.bath_tau_set(sd,approximated, tau_range)
            alpha_values[1] = residual.calculate_bath_tau_set(sd, approximated, tau_range)
            break
            # we only need the two rounds
            #here we concatinate the two list actually 
  

    if verbose:
        print(f"calculator_function: {calculator_function}")
        print(f"calculator an stelle{alpha_values}")

    for i in range(0,number_of_datapoints):
        for g in range(0,number_of_graphs):
            data_set[i].append(alpha_values[g][i])
    if verbose:
        print("data_set:",data_set)



    universal_plot.show(data_set,label)

if __name__ == "__main__":
    print('executed in main formatter...')

    #default
    spectral_density="debye"
    bose="compare"
    integral="numerical"
    plot = "num_compare"

    if len(sys.argv)>=5:
        spectral_density = sys.argv[2]
        bose = sys.argv[3]
        integral= sys.argv[4]
    if len(sys.argv)>2:
        plot = sys.argv[2]
    if plot=="num_compare":
        spectral_density = "compare" 
        bose = "closed" 
        integral="numerical"

    if plot=="num_debye":
        spectral_density="debye"
        bose = "laurent" 
        integral="compare"

    if plot=="bose_compare":
        spectral_density="debye"
        bose="compare"
        integral="numerical"
    print(f"format({spectral_density},{bose},{integral})")
    format(0,spectral_density,bose,integral)


        


