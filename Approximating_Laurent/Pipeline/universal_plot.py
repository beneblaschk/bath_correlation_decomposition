import matplotlib.pyplot as plt
import Parser_table_to_list as parser
import Plotting_debye as deb_plot
import numpy as np
import os
import data_sets as ds
#git_upload

#commit: 

# chat.gpt 
cmap = plt.get_cmap('viridis')


def show(data, label):

    for i in range(0,len(label)):
        label[i][1] = cmap(i/len(label))
        #chat.gpt code

    show_color(data, label,True)

def show_color(data, label,verbose): 
    """
    input: more dimensional array 
    first row is always tau values 
    next rows is values
    label: 
    """

    if verbose:
        print(f"received label: \n{label}")
        print(f"received data set: \n {data}")


    # Separate the data into two lists: one for each column
    tau_values = [row[0] for row in data]
    if verbose:
        print(f"tau valuse: {tau_values}")
    dimension = len(data[0])
    
    if verbose: 
        print(f"dimension: {dimension}")
    alpha_values = []
    for i in range(0, dimension-1):
        alpha_values.append([])

        alpha_values[i] = [row[i+1] for row in data]
        if verbose:
            print(f"alpha{i}, {alpha_values[i]}")

    # print(len(alpha_values))
    # print(len(tau_values))
    if verbose:
        print("alpha_values")
        print(alpha_values)
    # Create a plot
    plt.figure(figsize=(8, 5))
    #iterating overall values 
    for i in range(0, dimension-1):
        if verbose:
            print(f"alpha({i}) {alpha_values[0][i]}")
        plt.plot(tau_values, alpha_values[i], marker='o', linestyle='--', color=label[i][1], label=label[i][0])

    #plt.plot(tau_values, alpha_values[0], marker='o', linestyle='--', color= 'r', label="red")
    #plt.plot([i for i in range(1, 3)], [4,5,6], marker='o', linestyle='None', color= 'b', label="red")

    #ich versteh überhaupt nicht was grade mit dem plotter abgeht, er plottet einfach meine werte nicht


    # Set the labels and title
    plt.xlabel(r'$\tau$')
    plt.ylabel(r'$\alpha$')
    plt.title(r'Plot of $\alpha$ vs $\tau$')
    plt.grid(True)
    plt.legend()


    file_name= str(label[0][0]).replace(" ", "_")+".pdf"
    print(file_name)
    folder_path = "/home/benne/Documents/Uni/ba/bath/plots/"
    file_path = folder_path+file_name


    if not os.path.exists(file_path):
        plt.savefig(file_path, format='pdf')
        print(file_path+' saved')
        #only show when not existing! 
    
    # only show when no path
    plt.show()
if __name__ == "__main__":
    print('main')

    print(ds.debye_closed_numerics())
