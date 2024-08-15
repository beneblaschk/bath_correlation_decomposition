import matplotlib.pyplot as plt
import Parser_table_to_list as parser
import Plotting_debye as deb_plot
import numpy as np
import universal_plot
#git_upload


# mach mal mal nur 3 
# Parameter compare

#commit: 
# format: macht alle daten damit in den plotter rein können
# wir haben jetzt adjustable x-values! 
# - better label -> starts at 1 now! 


def format(compare,spectral_density,bose,integral):
    """
    input: configuration
    compare: what is compared
    spectral_density: which one is used: debye
    bose: laurent - closed? -taylor? 
    integral: residual - numerical
    """
    tau_range = [0]*3 
    tau_range[0] = 0.1 
    tau_range[1] = 2.0
    tau_range[2] = 0.1

    parameter_range = []
    parameter_range.append([])
    parameter_range[0] = [0]*3
    parameter_range[0][0] = 1 # eta = 1

    parameter_range.append([])
    parameter_range[1] = [0]*3

    parameter_range[1][0] = 1  # gamma =0,10.0, 0.1
    parameter_range[1][1] = 4
    parameter_range[1][2] = 1

    format_advanced_parameters(compare,spectral_density,bose,integral,tau_range, parameter_range)



def format_advanced_parameters(compare,spectral_density,bose,integral,tau_range, parameter_range):

    """
    input: configuration
    compare: what is compared
    spectral_density: which one is used: debye
    bose: laurent - closed? -taylor? 
    integral: residual - numerical
    tau_range (start,end, step-size)
    parametere_range (start, end, step-size) []
    """


    calculate_alpha_values = [] 
    
    if spectral_density=='debye':
        calculate_alpha_values.append(deb_plot.plot_debye_advanced_parameter)
        #man sollte hier tau einfach mit geben 
    else:
        return


    #TODO: einheitliche Parameter, also param[0] ... 
    # Tau Werte 
    tau_start = tau_range[0]
    tau_end = tau_range[1]
    tau_step_size = tau_range[2]



    eta = parameter_range[0][0]
    gamma_start = parameter_range[1][0]
    gamma_max= parameter_range[1][1]
    gamma_steps = parameter_range[1][2]

    #werte nicht immer neu ausrechnen sondern einfach ablegen und falls vorhanden dann verwenden!

    #residual_debye_values= [0.5146497652308826, 0.5410364229439333, 0.568775953527631, 0.5979377202573112, 0.6285946427394837, 0.6608233792488324, 0.6947045184138291, 0.7303227807302839, 0.7677672304067121, 0.8071314980712477, 0.8485140148969833, 0.8920182587311737, 0.9377530128437529, 0.9858326379421718, 1.036377358132735, 1.0895135615434877, 1.145374116360369, 1.2040987030668848, 1.2658341637180726, 1.3307348691221255, 1.3989631048478217, 1.4706894770229764, 1.546093338938626, 1.6253632395256772, 1.708697394825445, 1.7963041836330012, 1.8884026685527038, 1.9852231437688108, 2.087007710900895, 2.194010884384, 2.3065002278872977, 2.4247570233626283, 2.5490769743958954, 2.679770945620051, 2.8171657400386056, 2.961604916203358, 3.113449647289727, 3.2730796242178166, 3.440894005077489, 3.6173124132314998, 3.8027759865924793, 3.997748480697494, 4.202717428338437, 4.4181953586479725, 4.644721078689316, 4.882861020754545, 5.133210658740384, 5.396395997143096, 5.673075136395811, 5.963939918462385, 6.269717656802686, 6.591172955035078, 6.929109618843723, 7.284372665911497, 7.657850438904319, 8.05047682679056, 8.463233600049888, 8.89715286561085, 9.353319647655804, 9.832874600746523, 10.337016862054755, 10.867007049829752, 11.424170415600504, 12.009900157994883, 12.625660906461864, 13.272992383608067, 13.953513255306273, 14.668925178203207, 15.421017054747551, 16.21166950637782, 17.042859576055566, 17.91666567190256, 18.835272764303674, 19.800977849470996, 20.816195693130734, 21.883464868695413, 23.005454105019638, 24.18496895961229, 25.42495883399173, 26.72852434872576, 28.09892509659818, 29.539587793288543, 31.05411484594628, 32.64629336108491, 34.32010461432104, 36.079734005637114, 37.92958152506144, 39.874272754935156, 41.918670436277296, 44.06788662817045, 46.327295490571075, 48.70254672250868, 51.19957968927627, 53.82463827393707, 56.58428649028472, 59.48542489629665, 62.535307849123456, 65.74156164476018, 69.112203587759]

    #label = [["numerical_n=g=1",'r'],["residual_debye_0.5_1",'b'], ["residual_debye_1_1",'g']]


    # Example usage
    file_path = 'mathjax_array.txt'  # Replace with the path to your text file
    #data = parser.parse_mathjax_array_from_file("Pipeline/mathjax_array.txt")


    #TODO: color fix 
    colors = ['r', 'g', 'b', 'y', 'm', 'c', 'k', 'w', 'r', 'g']

    label = [] 

    for i in range(0,7):
        label.append([f"{eta}_{float(i*gamma_steps+gamma_start)}",f"{colors[i]}"])


    # hier werden die tau-Werte eingespeist
    data = [[round(i, 1)] for i in np.arange(tau_start,tau_end-0.1, tau_step_size)]
    #TODO: Warum ist hier -0.1 bei tau end?


    #Hier werden die alpha Werte eingespeist
    deb = [0]*gamma_max
    for g in range (gamma_start,gamma_max):
        deb[g] = calculate_alpha_values[0](1,g*gamma_steps,tau_range)

    # Hier werden die alpha werte alle zu einer Datenstruktur kombiniert 

    for i in range(0,len(data)):
        for g in range(gamma_start,gamma_max):
            data[i].append(deb[g][i])

    #show data
    universal_plot.show(data,label)

    #converting in the right format: 

if __name__ == "__main__":
    print('main')
    format(0,'debye','laurent','residual')



