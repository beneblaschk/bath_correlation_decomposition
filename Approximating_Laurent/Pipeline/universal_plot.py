import matplotlib.pyplot as plt
import Parser_table_to_list as parser

def plot_data(data):
    # Separate the data into two lists: one for each column
    tau_values = [row[0] for row in data]
    alpha_values = [row[1] for row in data]

    # Create a plot
    plt.figure(figsize=(8, 6))
    plt.plot(tau_values, alpha_values, marker='.', linestyle='None', color='r', label=r'$\alpha(\tau)$')

    # Set the labels and title
    plt.xlabel(r'$\tau$')
    plt.ylabel(r'$\alpha$')
    plt.title(r'Plot of $\alpha$ vs $\tau$')
    plt.grid(False)
    #plt.legend()

    # Show the plot
    plt.show()

# Example usage
file_path = 'mathjax_array.txt'  # Replace with the path to your text file
data = parser.parse_mathjax_array_from_file("Pipeline/mathjax_array.txt")
plot_data(data)
