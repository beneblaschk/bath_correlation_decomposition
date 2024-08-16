import matplotlib.pyplot as plt
import Parser_table_to_list as parser
import Plotting_debye as deb_plot
import numpy as np
import universal_plot
import math
#git_upload

#git changed
#changed again

# mach mal mal nur 3 
# Parameter compare

#commit: 



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
    tau_range[1] = 8
    tau_range[2] = 0.5

    parameter_range = []
    parameter_range.append([])
    parameter_range[0] = [0]*3
    parameter_range[0][0] = 1 # eta = 1

    parameter_range.append([])
    parameter_range[1] = [0]*3

    parameter_range[1][0] = 2.0  # gamma =0,10.0, 0.1
    parameter_range[1][1] = 2.5
    parameter_range[1][2] = 0.5




    format_advanced_parameters(compare,spectral_density,bose,integral,tau_range, parameter_range)



def format_advanced_parameters(compare,spectral_density,bose,integral,tau_range, parameter_range):

    format_advanced_parameter(compare, spectral_density, bose, integral, tau_range, parameter_range, 0)


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
    verbose = False
    if config<2:
        verbose = False
    else: 
        verbose = True 


    if config == 1: 
        print(f"tau: {tau_range[0]},{tau_range[1]},{tau_range[2]}") 
        print(f"gamma: {parameter_range[1][0]},{parameter_range[1][1]}, {parameter_range[1][2]}")

    calculate_alpha_values = [] 
    
    if spectral_density=='debye':
        if verbose:
            print('spectral density: debye spectral')
        calculate_alpha_values.append(deb_plot.plot_debye_advanced_parameter)
        #man sollte hier tau einfach mit geben 
    else:
        return

    # Tau Werte 
    tau_start = tau_range[0]
    tau_end = tau_range[1]
    tau_step_size = tau_range[2]
    if verbose:
        print(f"tau values: from {tau_range[0]} to {tau_range[1]} in {tau_range[2]} steps")

       # hier werden die tau-Werte eingespeist
    data_set = [[round(i, 1)] for i in np.arange(tau_start,tau_end, tau_step_size)]
    #TODO: Warum ist hier -0.1 bei tau end?
    # jetzt doch über die länge des arrays gelöst!
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


    number_of_graphs = int((gamma_max-gamma_start)/gamma_steps)
    if verbose:
        print(f"resulting in {number_of_graphs} graphs")
    # es wird wohl immer der letzte punkt rausgelassen, 
    #TODO fix the boundaries



    #werte nicht immer neu ausrechnen sondern einfach ablegen und falls vorhanden dann verwenden!

    #TODO: import values

    # Example usage
    file_path = 'mathjax_array.txt'  # Replace with the path to your text file
    #data = parser.parse_mathjax_array_from_file("Pipeline/mathjax_array.txt")


    label = [] 
    # nur label
    for i in range(0,number_of_graphs):
        label.append([f"{eta}_{float(i*gamma_steps+gamma_start)}",''])
    #TODO: color is managed in universal plot -> but also here -> left empty 

 

    #Hier werden die alpha Werte eingespeist
    alpha_values = [0]*number_of_graphs
    for g in range (0,number_of_graphs):
        alpha_values[g] = calculate_alpha_values[0](1,g*gamma_steps+gamma_start,tau_range)
        if verbose :
            print(f"alpha_value[{g}][2] = {alpha_values[g][2]} for this gamma: {g*gamma_steps+gamma_start}")

    if verbose: 
        print("alpha_values")
        print(alpha_values)


    # Hier werden die alpha werte an das leeere Data_set angehängt, sodass zu jedem tau wert der richtige alphawert passt 
    for i in range(0,number_of_datapoints):
        for g in range(0,number_of_graphs):
            data_set[i].append(alpha_values[g][i])

    #show data
    universal_plot.show(data_set,label)

    #converting in the right format: 

if __name__ == "__main__":
    print('executed in main formatter...')


    format(0,'debye','laurent','residual')



