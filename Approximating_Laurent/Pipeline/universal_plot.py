import matplotlib.pyplot as plt
import Parser_table_to_list as parser
import Plotting_debye as deb_plot
import numpy as np
#git_upload


def show(data, label):
    """
    input: more dimensional array 
    first row is always tau values 
    next rows is values
    label: 
    """
    #print(data)
    #print(label)


    # Separate the data into two lists: one for each column
    tau_values = [row[0] for row in data]
    dimension = len(data[0])
    alpha_values = []
    for i in range(0, dimension-1):
        alpha_values.append([])
        alpha_values[i] = [row[i+1] for row in data]
    

    # print(len(alpha_values))
    # print(len(tau_values))

    # Create a plot
    plt.figure(figsize=(14, 9))
    #iterating overall values 

    print(dimension)
    print(label)
    print(label[0][1])
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

if __name__ == "__main__":
    print('main')


