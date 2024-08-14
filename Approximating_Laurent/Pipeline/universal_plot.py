import matplotlib.pyplot as plt
import Parser_table_to_list as parser
import Plotting_debye as deb_plot
import numpy as np


def plot_data(data, label):
    # more dimensional array 
    # first row is always tau values 
    # and then it is 



    # Separate the data into two lists: one for each column
    tau_values = [row[0] for row in data]
    dimension = len(data[0])
    print(dimension)
    alpha_values = []
    for i in range(0, dimension):
        alpha_values.append([])
        alpha_values[i] = [row[i] for row in data]
    

    # print(len(alpha_values))
    # print(len(tau_values))

    # Create a plot
    plt.figure(figsize=(14, 9))
    #iterating overall values 
    for i in range(0, dimension-1):
        plt.plot(tau_values, alpha_values[i], marker='.', linestyle='None', color=label[i][1], label=label[i][0])



    # Set the labels and title
    plt.xlabel(r'$\tau$')
    plt.ylabel(r'$\alpha$')
    plt.title(r'Plot of $\alpha$ vs $\tau$')
    plt.grid(True)
    plt.legend()

    # Show the plot
    plt.show()


residual_debye_values= [0.5146497652308826, 0.5410364229439333, 0.568775953527631, 0.5979377202573112, 0.6285946427394837, 0.6608233792488324, 0.6947045184138291, 0.7303227807302839, 0.7677672304067121, 0.8071314980712477, 0.8485140148969833, 0.8920182587311737, 0.9377530128437529, 0.9858326379421718, 1.036377358132735, 1.0895135615434877, 1.145374116360369, 1.2040987030668848, 1.2658341637180726, 1.3307348691221255, 1.3989631048478217, 1.4706894770229764, 1.546093338938626, 1.6253632395256772, 1.708697394825445, 1.7963041836330012, 1.8884026685527038, 1.9852231437688108, 2.087007710900895, 2.194010884384, 2.3065002278872977, 2.4247570233626283, 2.5490769743958954, 2.679770945620051, 2.8171657400386056, 2.961604916203358, 3.113449647289727, 3.2730796242178166, 3.440894005077489, 3.6173124132314998, 3.8027759865924793, 3.997748480697494, 4.202717428338437, 4.4181953586479725, 4.644721078689316, 4.882861020754545, 5.133210658740384, 5.396395997143096, 5.673075136395811, 5.963939918462385, 6.269717656802686, 6.591172955035078, 6.929109618843723, 7.284372665911497, 7.657850438904319, 8.05047682679056, 8.463233600049888, 8.89715286561085, 9.353319647655804, 9.832874600746523, 10.337016862054755, 10.867007049829752, 11.424170415600504, 12.009900157994883, 12.625660906461864, 13.272992383608067, 13.953513255306273, 14.668925178203207, 15.421017054747551, 16.21166950637782, 17.042859576055566, 17.91666567190256, 18.835272764303674, 19.800977849470996, 20.816195693130734, 21.883464868695413, 23.005454105019638, 24.18496895961229, 25.42495883399173, 26.72852434872576, 28.09892509659818, 29.539587793288543, 31.05411484594628, 32.64629336108491, 34.32010461432104, 36.079734005637114, 37.92958152506144, 39.874272754935156, 41.918670436277296, 44.06788662817045, 46.327295490571075, 48.70254672250868, 51.19957968927627, 53.82463827393707, 56.58428649028472, 59.48542489629665, 62.535307849123456, 65.74156164476018, 69.112203587759]

#label = [["numerical_n=g=1",'r'],["residual_debye_0.5_1",'b'], ["residual_debye_1_1",'g']]




# Example usage
file_path = 'mathjax_array.txt'  # Replace with the path to your text file
#data = parser.parse_mathjax_array_from_file("Pipeline/mathjax_array.txt")

# mach mal mal nur 3 
eta = 1
gamma_max=10
gamma_steps = 0.12

colors = ['r', 'g', 'b', 'y', 'm', 'c', 'k', 'w', 'r', 'g']

label = [] 

for i in range(0,gamma_max):
    label.append([f"{eta}_{i*gamma_steps}",f"{colors[i]}"])

print(label)

deb = [0]*gamma_max
τ_values = np.arange(0.1,9.9, 0.1)

data = [[round(i, 1)] for i in np.arange(0.1, 10.0, 0.1)]

for g in range (0,gamma_max):
    deb[g] = deb_plot.plot_debye(1,g*gamma_steps)


for i in range(0,len(data)):
    for g in range(0,gamma_max):
        data[i].append(deb[g][i])

#print(data)
plot_data(data,label)


#converting in the right format: 




