import matplotlib.pyplot as plt
import Parser_table_to_list as parser
import Plotting_debye as deb_plot
import numpy as np
import universal_plot
import math
import integrate_quad_cleaned
import sys
#git_upload

#commit: 
# ich glaub ich hab ausversehen die data_poitns und gaphs verwechselt


sd = [0]*3
sd[0] = "debye"
sd[1] = "ohmic"
sd[2] = "ultra_violet_cutoff"


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
    tau_range[1] = 10    #es sollte eigenlich bis 2 gehen jetzt
    tau_range[2] = 0.5

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

    eta = parameter_range[0][0]
    gamma_start = parameter_range[1][0]
    gamma_max= parameter_range[1][1]
    gamma_steps = parameter_range[1][2]
    if verbose:
        print(f"gamma values: from {parameter_range[1][0]} to {parameter_range[1][1]} in {parameter_range[1][2]} steps")

    # that is only when parameter compare haben!

    #number_of_graphs = int((gamma_max-gamma_start)/gamma_steps)

    # es wird wohl immer der letzte punkt rausgelassen, 
    #TODO fix the boundaries



    #werte nicht immer neu ausrechnen sondern einfach ablegen und falls vorhanden dann verwenden!

    #TODO: import values

    # Example usage
    file_path = 'mathjax_array.txt'  # Replace with the path to your text file
    #data = parser.parse_mathjax_array_from_file("Pipeline/mathjax_array.txt")


    label = [] 
    # nur label
    if integral=='residual':
        for i in range(0,number_of_graphs):
            label.append([f"{eta}_{float(i*gamma_steps+gamma_start)}",''])
             #TODO: color is managed in universal plot -> but also here -> left empty 


    # We have 3 configurations:
    # spectral density 
    # bose
    # integral 

    #mabye also sd parameter compare

    # each of them can be fixed, or compare to compare it

    # spectral density-> einfach auf die jeweilige setzen dann 
    # bose -> approximated or not
    # integral -> selecting the right function 




    if spectral_density=="compare":
        print("not yet implemented")
        return
    #therefore is a spectral_density now fixed
    sd = spectral_density # mabye also the array
    if verbose:
        print('spectral density: debye spectral')

    if bose=="compare":
        number_of_graphs=2
        if verbose:
            print('compare bose')
        # we only have two graphs to compare

    # Bose should be closed for now
    approximated = False

    if integral=="compare":
        print("not yet implemented")
        return
    if integral=="residual":
        calculator_function= deb_plot.plot_residual
        return
        # adding the residual plotter has only debye -> because advanced calculation...

    if integral=="numerical":
        if verbose:
            print("adding integratie quad to calculator_function")
        calculator_function= integrate_quad_cleaned.bath_tau_set
    
    if verbose:
        print(f"resulting in {number_of_graphs} graphs")

    # now the calculator function is applied
    calculate_alpha_values = [0]*number_of_graphs
    for i in range (0, number_of_graphs):
        if bose=="compare":
            calculate_alpha_values[i]= calculator_function(sd,not (i%2==0),tau_range)    # ich will mit false anfangen (closed), modulo weil dann ist es einmal true und einmal false
            continue
        if spectral_density=="compare":
            calculate_alpha_values[i]= calculator_function(sd[i],approximated,tau_range)
        else:
            calculate_alpha_values[i]= calculator_function(sd[i],approximated,tau_range)
        # integral sollte eigentlich fine sein schon weil die funktion ja schon richtig ausgewählt ist
     

    if verbose:
        print(f"calculator_function: {calculator_function}")
        print(f"calculator an stelle{calculate_alpha_values}")
    


    # if integral=='compare':
    # #also dieser bereich soll verglichen werden: 
    #         label.append([f"numerical",''])
    #         label.append([f"residual",''])



    #         #parameter starts
    #         parameter_range[0][0] = 1
    #         parameter_range[1][0] = 1
    #         number_of_graphs = 2
    #         calculate_alpha_values = [0]*number_of_graphs
    #         calculate_alpha_values[0]=integrate_quad_cleaned.bath_closed_tau_set
    #         calculate_alpha_values[1]=deb_plot.plot_debye_advanced_parameter
                   

    # if spectral_density=="compare":
    #         label.append([f"{sd[0]}",''])
    #         label.append([f"{sd[1]}",''])
    #         label.append([f"{sd[2]}",''])        
    #         calculate_alpha_values[0]=integrate_quad_cleaned.bath_tau_set
    #         calculate_alpha_values[1]=integrate_quad_cleaned.bath_tau_set
    #         calculate_alpha_values[2]=integrate_quad_cleaned.bath_tau_set
    #         number_of_graphs =3
 

    #Hier werden die alpha Werte eingespeist
    alpha_values = [0]*number_of_graphs
    if verbose: 
        print(alpha_values)


    # man könnte auch einfach die number_of_graphs literally nehmen und einfach dann nicht die gammas
    # variiern sondern wirklich die zwei veschiedenen graphen rein hauen


    # ich überschreibe hier die daten wieder!
    if verbose:
        print(f"number of graphs {number_of_graphs}")
    
    for g in range (0,number_of_graphs):
        if integral == 'compare':
            alpha_values[g] = calculate_alpha_values[g](1,gamma_start,tau_range)

        # jetzt werden einfach zwei verschiedene funktionen verwendet um zu plotten 
        if spectral_density=="compare":
            #normaler case mit gamma variation
            alpha_values[g] = calculate_alpha_values[0](sd[g],approximated,tau_range)
        else:    
            alpha_values[g] = calculate_alpha_values[0](1,g*gamma_steps+gamma_start,tau_range)

        


        if verbose :
            print(f"alpha_value[{g}] = {alpha_values[g]} len: {len(alpha_values[g])}")
            #print(f"alpha_value[{g}][2] = {alpha_values[g][2]} for this gamma: {g*gamma_steps+gamma_start}")
    
  



    if verbose: 
        print("alpha_values")
        print(alpha_values)
    #number_of_graphs =2  -> ich glaub das war nur für den anderen fall mit compare
    # Hier werden die alpha werte an das leeere Data_set angehängt, sodass zu jedem tau wert der richtige alphawert passt 
    for i in range(0,number_of_datapoints):
        for g in range(0,number_of_graphs):
            data_set[i].append(alpha_values[g][i])

    #show data
    universal_plot.show(data_set,label)

    #converting in the right format: 

if __name__ == "__main__":
    print('executed in main formatter...')

    plot = "num_compare"

    if len(sys.argv)>2:
        plot = sys.argv[2]
        print(plot)
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


        


