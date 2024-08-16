import matplotlib.pyplot as plt
import Parser_table_to_list as parser
import Plotting_debye as deb_plot
import numpy as np
#git_upload

#commit: 
# color fixed here with colormap -> color gradient
# layout changed to dotted lines and bigger points

# Create a colormap
cmap = plt.get_cmap('viridis')


def show(data, label):

    for i in range(0,len(label)):
        label[i][1] = cmap(i/len(label))


    show_color(data, label)

def show_color(data, label): 
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
    for i in range(0, dimension-1):
        plt.plot(tau_values, alpha_values[i], marker='o', linestyle='--', color=label[i][1], label=label[i][0])



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


