import matplotlib.pyplot as plt
import numpy as np


# Example data
x = np.linspace(0, 10, 100)
y = [np.sin(x + phase) for phase in np.linspace(0, 2*np.pi, 10)]

# Create a colormap
cmap = plt.get_cmap('viridis')


# Data
x_values = np.array([-10.00, -9.00, -8.00, -7.00, -6.00, -5.00, -4.00, -3.00, -2.00, -1.00,
                       0.00, 1.00, 2.00, 3.00, 4.00, 5.00, 6.00, 7.00, 8.00, 9.00, 10.00])
lauren_values = [0]*10 

reference_values=np.array([ -0.0000, -0.0001, -0.0003, -0.0009, -0.0025, -0.0068, -0.0187, -0.0524, -0.1565, -0.5820, 1.5820, 1.1565, 1.0524, 1.0187, 1.0068, 1.0025, 1.0009, 1.0003, 1.0001, 1.0000, 0])

lauren_values[1]=np.array([ -0.1000, -0.1111, -0.1250, -0.1429, -0.1667, -0.2000, -0.2500, -0.3333, -0.5000, -1.0000, 1.0000, 0.5000, 0.3333, 0.2500, 0.2000, 0.1667, 0.1429, 0.1250, 0.1111, 0.1000, 0])
lauren_values[2]=np.array([ 0.4000, 0.3889, 0.3750, 0.3571, 0.3333, 0.3000, 0.2500, 0.1667, 0.0000, -0.5000, 1.5000, 1.0000, 0.8333, 0.7500, 0.7000, 0.6667, 0.6429, 0.6250, 0.6111, 0.6000, 0])
lauren_values[3]=np.array([ -0.4333, -0.3611, -0.2917, -0.2262, -0.1667, -0.1167, -0.0833, -0.0833, -0.1667, -0.5833, 1.5833, 1.1667, 1.0833, 1.0833, 1.1167, 1.1667, 1.2262, 1.2917, 1.3611, 1.4333, 0])
lauren_values[4]=np.array([ 0.9556, 0.6514, 0.4194, 0.2502, 0.1333, 0.0569, 0.0056, -0.0458, -0.1556, -0.5819, 1.5819, 1.1556, 1.0458, 0.9944, 0.9431, 0.8667, 0.7498, 0.5806, 0.3486, 0.0444, 0])
lauren_values[5]=np.array([ -2.3513, -1.3013, -0.6642, -0.3056, -0.1238, -0.0464, -0.0283, -0.0539, -0.1566, -0.5820, 1.5820, 1.1566, 1.0539, 1.0283, 1.0464, 1.1238, 1.3056, 1.6642, 2.3013, 3.3513, 0])
lauren_values[6]=np.array([ 5.9159, 2.6529, 1.0696, 0.3753, 0.1076, 0.0182, -0.0148, -0.0521, -0.1565, -0.5820, 1.5820, 1.1565, 1.0521, 1.0148, 0.9818, 0.8924, 0.6247, -0.0696, -1.6529, -4.9159, 0])
lauren_values[7]=np.array([ -14.9609, -5.4352, -1.7324, -0.4672, -0.1028, -0.0226, -0.0202, -0.0525, -0.1565, -0.5820, 1.5820, 1.1565, 1.0525, 1.0202, 1.0226, 1.1028, 1.4672, 2.7324, 6.4352, 15.9609, 0])
lauren_values[8]=np.array([ 37.8810, 11.1471, 2.8067, 0.5777, 0.0889, 0.0032, -0.0180, -0.0524, -0.1565, -0.5820, 1.5820, 1.1565, 1.0524, 1.0180, 0.9968, 0.9111, 0.4223, -1.8067, -10.1471, -36.8810, 0])
lauren_values[9]=np.array([ -95.9443, -22.8695, -4.5505, -0.7190, -0.0858, -0.0131, -0.0189, -0.0524, -0.1565, -0.5820, 1.5820, 1.1565, 1.0524, 1.0189, 1.0131, 1.0858, 1.7190, 5.5505, 23.8695, 96.9443, 0])
# Plot
plt.figure(figsize=(12, 6))

# Plot with different colors

#reference in red
plt.plot(x_values, reference_values, 'ro', label='Reference Values')


for i in range(1,10):
    color = cmap(i / 10)  # Get a color from the colormap
    plt.plot(x_values, lauren_values[i], color=color,linestyle="-.", label=f"n={i}")
    # supported values are '-', '--', '-.', ':', 'None', ' ', '', 'solid', 'dashed', 'dashdot', 'dotted'




plt.xlabel('x')
plt.ylabel('Value')
plt.ylim(-10,10)
plt.title('Comparison of Laurent Function and Reference Values')
plt.legend()
plt.grid(True)

plt.show()
