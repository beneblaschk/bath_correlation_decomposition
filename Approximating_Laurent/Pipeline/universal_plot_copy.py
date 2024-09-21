import matplotlib.pyplot as plt
import Parser_table_to_list as parser
import Plotting_debye as deb_plot
import numpy as np
import os
import data_sets as ds
import sys
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

    tau_values= [0.0,1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0, 21.0, 22.0, 23.0, 24.0, 25.0, 26.0, 27.0, 28.0, 29.0,30.0]
    plt.figure(figsize=(8, 5))
    #iterating overall values 
    for i in range(0, len(data)):
        plt.plot(tau_values, data[i], marker='o', linestyle='--', color=colors[i], label=labels[i])

    plt.xlabel(r'$\tau$')
    plt.ylabel(r'$\alpha$')
    plt.title(r'Plot of $\alpha$ vs $\tau$')
    plt.grid(True)
    plt.legend()
    #plt.yscale('log')

    file_name= str(label[0]).replace(" ", "_")+".pdf"
    file_name= f"{str(len(sys.argv)-1)}_{str(sys.argv[1])}.pdf"

    print(file_name)
    folder_path = "/home/benne/Documents/Uni/ba/bath/plots/numeric_framework/"
    file_path = folder_path+file_name


    plt.savefig(file_path, format='pdf')
    print(file_path+' saved')
    plt.show()
if __name__ == "__main__":
    print('main')
    mode = 11
    if mode ==1:

        data = [0,0,0,0]
        label = ["","","",""]
        data[0] = ds.debye_closed_numerics
        data[1] = ds.debye_closed_residual
        data[2] = ds.ohmic_closed_numerics
        data[3] = ds.ohmic_closed_residual

        print(data[0])
        print(len(data[0]))
        label[0] = "debye_closed_numerics_a=-100_b=100_e=0.01"
        label[1] = "debye_closed_residuals_K=5"
        label[2] = "ohmic_closed_numerics_a=-100_b=100_e=0.01"
        label[3] = "ohmic_closed_residuals_K=5"
    if mode ==2: 
        data = [0,0,0,0]
        label = ["","","",""]
        data[0] = ds.debye_closed_numerics
        data[1] = ds.debye_laurent_numerics
        data[2] = ds.ohmic_closed_numerics
        data[3] = ds.ohmic_laurent_numerics

        print(data[0])
        print(len(data[0]))
        label[0] = "debye_closed_numerics_a=-100_b=100_e=0.01_C"
        label[1] = "debye_laurent_numerics_a=-100_b=100_e=0.01_N=2_C"
        label[2] = "ohmic_closed_numerics_a=-100_b=100_e=0.01"
        label[3] = "ohmic_laurent_numerics_a=-100_b=100_e=0.01"
    if mode ==3: 
        data = [0,0]
        label = ["",""]
        data[0] = ds.debye_closed_residual
        data[1] = ds.ohmic_closed_residual

        print(data[0])
        print(len(data[0]))
        label[0] = "debye_closed_residuals_K=5"
        label[1] = "ohmic_closed_residuresidual_K=5"      
    if mode ==4: 
        data = [0,0]
        label = ["",""]
        data[0] = ds.debye_closed_numerics
        data[1] = ds.debye_closed_residual

        print(data[0])
        print(len(data[0]))
        label[0] = "debye_closed_numerics_a=-100_b=100_e=0.01_C"
        label[1] = "debye_closed_residuals_K=5"   
    if mode ==5: 
        data = [0,0]
        label = ["",""]
        data[0] = ds.debye_closed_numerics
        data[1] = ds.ohmic_closed_numerics

        print(data[0])
        print(len(data[0]))
        label[0] = "debye_closed_numerics_a=-100_b=100_e=0.01"
        label[1] = "ohmic_closed_numerics_a=-100_b=100_e=0.01"

    if mode == 6:
        data = [0,0]
        label = ["",""]
        data[0] = ds.ohmic
        data[1] = ds.ohmic
        print(data[0])
        print(len(data[0]))
        label[0] = "debye_spectral_density"
        label[1] = "ohmic_spectral_density"
    if mode == 7:
        data = [0]
        label = [""]
        data[0] = ds.debye
        print(data[0])
        print(len(data[0]))
        label[0] = "debye_spectral_density"

    if mode == 8:
        data = [0,0]
        label = ["",""]
        label[0] = "debye_closed_numerics_a=-100_b=100_e=0.01"
        label[1] = "debye_closed_residuals_K=5"  
        data[0] = ds.debye_closed_numerics
        data[1] = ds.debye_closed_residual_first_term
        print(data[0])
        print(data[1])
        print(len(data[0]))
        print(len(data[1]))
    if mode == 9:
        label=[""]*8
        data= [0]*8
        label[0] = "debye_closed_numerics_a=-1_b=1_e=0.01"
        data[0]  = ds.debye_closed_numerics_1
        label[1] = "debye_closed_numerics_a=-2_b=2_e=0.01"
        data[1]  = ds.debye_closed_numerics_2
        label[2] = "debye_closed_numerics_a=-4_b=4_e=0.01"
        data[2]  = ds.debye_closed_numerics_4
        label[3] = "debye_closed_numerics_a=-8_b=8_e=0.01"
        data[3]  = ds.debye_closed_numerics_8
        label[4] = "debye_closed_numerics_a=-16_b=16_e=0.01"
        data[4]  = ds.debye_closed_numerics_16
        label[5] = "debye_closed_numerics_a=-32_b=32_e=0.01"
        data[5]  = ds.debye_closed_numerics_32  
        label[6] = "debye_closed_numerics_a=-64_b=64_e=0.01"
        data[6]  = ds.debye_closed_numerics_64
        label[7] = "debye_closed_numerics_a=-128_b=128_e=0.01"
        data[7]  = ds.debye_closed_numerics_128
        show(data,label)
        exit
    if mode==10:
        label=[""]*3
        data= [0]*3
        label[0] = "debye_closed_numerics_a=-16_b=16_e=0.01"
        data[0]  = ds.debye_closed_numerics_16
        label[1] = "debye_closed_numerics_a=-64_b=64_e=0.01"
        data[1]  = ds.debye_closed_numerics_64
        label[2] = "debye_closed_numerics_a=-128_b=128_e=0.01"
        data[2]  = ds.debye_closed_numerics_128
        show(data,label)
        exit
    if mode == 11:
        label=[""]*7
        data= [0]*7
        label[0] = "debye_closed_numerics_a=-16_b=16_e=0.1"
        data[0]  = ds.debye_closed_numerics_e_0_1
        label[1] = "debye_closed_numerics_a=-16_b=16_e=0.05"
        data[1]  = ds.debye_closed_numerics_e_0_05
        label[2] = "debye_closed_numerics_a=-16_b=16_e=0.01"
        data[2]  = ds.debye_closed_numerics_e_0_01
        label[3] = "debye_closed_numerics_a=-16_b=16_e=0.005"
        data[3]  = ds.debye_closed_numerics_e_0_005
        label[4] = "debye_closed_numerics_a=-16_b=16_e=0.001"
        data[4]  = ds.debye_closed_numerics_e_0_001
        label[5] = "debye_closed_numerics_a=-16_b=16_e=0.0005"
        data[5]  = ds.debye_closed_numerics_e_0_0005
        label[6] = "debye_closed_numerics_a=-16_b=16_e=0.0001"
        data[6]  = ds.debye_closed_numerics_e_0_0001
        show(data,label)
        exit(0)
    number_graphs = len(sys.argv)-1
    label = [""]*number_graphs
    data = [0] *number_graphs
    for i in range(0,number_graphs):
        value = str(sys.argv[i+1])
        label[i] = value
        match value:
            case "debye_closed_numerics":
                #data[i] = ds.debye_closed_numerics
                data[i] = ds.debye_closed_numerics_16
            case "debye_closed_residuals":
                data[i] = ds.debye_closed_residuals
            case "debye_approxed_numerics":
                data[i] = ds.debye_closed_numerics
            case "debye_approxed_residuals":
                exit
            case "ohmic_closed_numerics":
                data[i] = ds.ohmic_closed_numerics
            case "ohmic_closed_residuals":
                data[i] = ds.ohmic_closed_residuals
            case "ohmic_approxed_numerics":
                data[i] = ds.ohmic_laurent_numerics
            case "ohmic_approxed_residuals":
                exit
            case "debye_laurent_residual":
                data[i] = ds.debye_laurent_residual
            case "debye_closed_residuals_imag":
                data[i] = ds.debye_closed_residuals_imag
            case "debye_closed_numerics_imag":
                data[i] = ds.debye_closed_numerics_imag
            case "ohmic_closed_residuals_imag":
                data[i] = ds.ohmic_closed_residuals_imag
            case "ohmic_closed_numerics_imag":
                data[i] = ds.ohmic_closed_numerics_imag
            case "ohmic_closed_diff":
                data[i] = ds.ohmic_closed_diff
            case "debye_closed_diff":
                data[i] = ds.debye_closed_diff
            case "debye_closed_numerics_T_2":
                data[i] = ds.debye_closed_numerics_T_2
            case "debye_closed_numerics_T_002":
                data[i] = ds.debye_closed_numerics_T_002
            case "debye_closed_residuals_T_002":
                data[i] = ds.debye_closed_residuals_T_002
            case "debye_closed_residuals_mod_1":
                data[i] = ds.debye_closed_residuals_mod_1
            case "debye_closed_residuals_mod_2":
                data[i] = ds.debye_closed_residuals_mod_2
            case "deb_res_k=1":
                data[i] = ds.debye_closed_residuals_mod_5_k_1
            case "deb_res_k=2":
                data[i] = ds.debye_closed_residuals_mod_5_k_2
            case "deb_res_k=3":
                data[i] = ds.debye_closed_residuals_mod_5_k_3
            case "deb_res_k=4":
                data[i] = ds.debye_closed_residuals_mod_5_k_4
            case "deb_res_k=5":
                data[i] = ds.debye_closed_residuals_mod_5_k_5

                                                         
            case _:
                print("error")
                exit
    # print(number_graphs)
    # print(data)
    # print(label)
    # print(len(data[0]))

    show(data,label)
