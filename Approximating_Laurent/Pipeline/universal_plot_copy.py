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


def show(data, labels):
    number_graphs= len(data)
    colors = [0]* number_graphs
    for i in range(0,number_graphs):
        colors[i] = cmap(i/len(label))
        #chat.gpt code

    tau_values= [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0, 21.0, 22.0, 23.0, 24.0, 25.0, 26.0, 27.0, 28.0, 29.0, 30.0]
    plt.figure(figsize=(8, 5))
    #iterating overall values 
    for i in range(0, len(data)):
        plt.plot(tau_values, data[i], marker='o', linestyle='--', color=colors[i], label=labels[i])

    plt.xlabel(r'$\tau$')
    plt.ylabel(r'$\alpha$')
    plt.title(r'Plot of $\alpha$ vs $\tau$')
    plt.grid(True)
    plt.legend()


    file_name= str(label[0]).replace(" ", "_")+".pdf"
    print(file_name)
    folder_path = "/home/benne/Documents/Uni/ba/bath/plots/"
    file_path = folder_path+file_name


    plt.savefig(file_path, format='pdf')
    print(file_path+' saved')
    plt.show()
if __name__ == "__main__":
    print('main')

    data = [0]
    label = [""]
    data[0] = ds.debye_closed_numerics
    print(data[0])
    print(len(data[0]))
    label[0] = "debye_closed_numerics"
    show(data,label)