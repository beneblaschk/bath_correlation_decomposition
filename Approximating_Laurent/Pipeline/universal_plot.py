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

    plt.figure(figsize=(8, 5))
    #iterating overall values 
    for i in range(0, len(data)-1):
        plt.plot(tau_values, alpha_values[i], marker='o', linestyle='--', color=label[i][1], label=label[i][0])

    plt.xlabel(r'$\tau$')
    plt.ylabel(r'$\alpha$')
    plt.title(r'Plot of $\alpha$ vs $\tau$')
    plt.grid(True)
    plt.legend()


    file_name= str(label[0][0]).replace(" ", "_")+".pdf"
    print(file_name)
    folder_path = "/home/benne/Documents/Uni/ba/bath/plots/"
    file_path = folder_path+file_name


    
    plt.savefig(file_path, format='pdf')
    print(file_path+' saved')
    #only show when not existing! 
    
    # only show when no path
    plt.show()
if __name__ == "__main__":
    print('main')

    print(ds.tau_values)

